import requests
import re
import json
import time
global header
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Content-Type': 'application/json',
    'Referer': 'https://kimi.moonshot.cn',
    'Origin': 'https://kimi.moonshot.cn'
}
class Config:
    def __init__(self, config_file):
        self.config_file = config_file

    def load_config(self):
        return json.load(open(self.config_file, encoding='utf-8'))

    def write_config(self, accesstoken, refresh_token):
        config = self.load_config()
        config['access_token'] = accesstoken
        config['refresh_token'] = refresh_token
        with open(self.config_file, 'w', encoding='utf-8') as w:
            w.write(json.dumps(config))

    def config_newer(self):
        refresh_token = self.load_config()['refresh_token']
        header['Authorization'] = refresh_token
        response = requests.get('https://kimi.moonshot.cn/api/auth/token/refresh', headers=header).json()
        accesstoken, refresh_token = list(response.values())
        refresh_token = f'Bearer {refresh_token}'
        accesstoken = f'Bearer {accesstoken}'
        self.write_config(accesstoken, refresh_token)

class Chat:
    def __init__(self, config_instance):
        self.config = config_instance

    def chat_start(self, chatserial):
        return f'https://kimi.moonshot.cn/api/chat/{chatserial}/completion/stream'

    def new_chat(self, title):
        header['Authorization'] = self.config.load_config()['access_token']
        response = requests.post('https://kimi.moonshot.cn/api/chat', headers=header, json={'name': title}).json()
        return response['id']

    def chat_main(self, messages):
        header['Authorization'] = self.config.load_config()['access_token']
        chatserial = self.new_chat('新一轮对话')
        chat_url = self.chat_start(chatserial)
        concat_content = ''
        for msg in messages:
            role, content = msg['role'], msg['content']
            single_msg = f'{role}: {content}\n\n'
            concat_content += single_msg
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, concat_content)
        for url in urls:
            new_url = f'<url id="" type="url" status="" title="" wc="">{url}</url>'
            concat_content = concat_content.replace(url, new_url)
        concat_msg = [{'content': concat_content, 'role': 'user'}]
        response = requests.post(chat_url, headers=header, json={'messages': concat_msg})
        return response

    def read_question(self):
        with open("question.json", "r", encoding="utf-8") as f:
            question = f.read()
        return question

    def call(self, question):
        prompt = [{'content': question, 'role': 'user'}]
        response = self.chat_main(prompt)
        row = []
        for chunk in response.iter_lines(chunk_size=1024):
            row.append(chunk)
        extracted_text = ''
        rowstr = []
        for chunk in row:
            chunk_str = chunk.decode('utf-8').replace('data: ', '')
            if chunk_str is not None:
                rowstr.append(chunk_str)
        for js_str in rowstr:
            try:
                js_obj = json.loads(js_str)
                text_value = js_obj.get('text', '')
                if text_value:
                    extracted_text += text_value
            except json.JSONDecodeError:
                continue

        print(extracted_text)
        with open("response.json", "w") as outfile:
            json.dump(extracted_text, outfile)

    def interact(self):
        time.sleep(1)
        question = input("请输入问题：")
        self.call(question)

if __name__ == '__main__':
    config = Config('config.json')
    config.config_newer()
    chat = Chat(config)
    while True:
        chat.interact()
