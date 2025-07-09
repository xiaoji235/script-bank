# 欢迎来到script-bank
这里是存放各类脚本，可使用curl拉取并运行在设备上

## ollama linux版下载（特快CDN，使用前请安装curl或wget）
 - 标准版：`curl -fsSL https://cdn.jsdelivr.net/gh/xiaoji235/script-bank/ollama/install.sh | sh`
 - 汉化版：`curl -fsSL https://cdn.jsdelivr.net/gh/xiaoji235/script-bank/ollama/install-zh_CN.sh | sh`
### 以下是安卓Termux一键安装命令：
1.5b版本：
`sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list && pkg update && pkg install wget -y && wget https://gh.zhaojun.im/https://github.com/xiaoji235/script-bank/blob/main/ollama/ollama-android.sh && bash ollama-android.sh`<br>
7b版本：
`sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list && pkg update && pkg install wget -y && wget https://gh.zhaojun.im/https://github.com/xiaoji235/script-bank/blob/main/ollama/ollama-android-7b.sh && bash ollama-android-7b.sh`<br>
8b版本：
`sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list && pkg update && pkg install wget -y && wget https://gh.zhaojun.im/https://github.com/xiaoji235/script-bank/blob/main/ollama/ollama-android-8b.sh && bash ollama-android-8b.sh`<br>
14b版本：
`sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list && pkg update && pkg install wget -y && wget https://gh.zhaojun.im/https://github.com/xiaoji235/script-bank/blob/main/ollama/ollama-android-14b.sh && bash ollama-android-14b.sh`<br>
