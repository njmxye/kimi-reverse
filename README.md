# *仅限学习研究使用，禁止用作非法用途，非法使用造成的一切后果自行承担！！！
# 🚀 Kimi大模型逆向测试与研究 🚀
## 🤖 项目简介 🤖
本项目致力于对Kimi大模型进行深入的逆向测试与研究，旨在探索编程技术。🔍
## 🎯 项目现状 🎯
- 经笔者测试正确配置后可以正常进行对话，暂时没有bug！
## 📌 目前项目痛点 📌
- 第一次使用需要手动填写config文件
- 缺少记忆上下文功能
- 缺少api的功能，只作为逆向的初探与研究
- 长时间的使用（数个小时）可能导致对话token的失效
- 如果遇到持续使用时token失效问题，关闭终端重新运行脚本即可，因为我已经写过了自动刷新token的逻辑。
## 🎯 目标受众 🎯
- AI爱好者
- 机器学习研究者
- 开源社区成员
## 📚 使用说明 📚
- 1. **克隆项目**：`git clone https://github.com/njmxye/kimi-reverse.git`
- 2. **进入根目录**：`cd kimi-reverse`
- 3. **确保电脑有python3环境**：不懂自行百度下载python3以上环境
- 4. **安装依赖**：`pip install -r requirements.txt`
- 5. **开始研究**：遵循项目目录结构，逐步深入了解Kimi大模型
## 🚀 使用方法 🚀
- 1. **填写config.json文件**：
根据自己的需求修改config.json文件，两个cookies的格式均为Bearer xxx，xxx代表了你自己的实际cookies，具体获取方法请去kimi官网登录并进行一次对话，f12的应用程序里的本地存储里的refresh_token和access_token值
### **请注意，那两个token的值是不一样的（不会获取请自行百度！）**。
记住，建议每次长时间未使用脚本（几天未使用）建议重新填写一个这个cookies，否则可能会被kimi视为身份验证无效。
- 2. **运行脚本**：`python main.py`
- 3. **在命令行输入问题，开始无限对话**
## 📢 重要提醒 📢
- **仅供学习研究**：本项目仅供学术研究使用，禁止用于任何商业及违法活动。
- **后果自负**：如因使用者个人行为导致法律风险，责任由使用者自负。🚫
## 🤝 参与贡献 🤝
欢迎各位大佬加入我们，一起探索Kimi大模型的奥秘！🌟
## 📞 联系我们 📞
如有疑问或建议，请通过以下方式与我们联系：
- Issue：在本项目中创建issue
感谢您的关注与支持！🙏
--- 
🔥 **声明**：本项目遵循开源协议，请遵守相关法律法规，共同维护网络秩序。🔥
## ©️ Copyright

This program is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```
njmxye/kimi-reverse: Copyright (C) 2024 njmxye

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```


