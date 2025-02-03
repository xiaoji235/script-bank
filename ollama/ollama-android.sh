#!/bin/sh

# Function to repeat a command until it succeeds
repeat_until_success() {
  while true; do
    "$@" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
      echo "成功: $*"
      break
    else
      echo "正在重试: $*"
      sleep 2
    fi
  done
}

echo "正在安装依赖..."
repeat_until_success apt install git golang python cmake clang -y

echo "正在复制仓库..."
repeat_until_success git clone https://gh.zhaojun.im/https://github.com/ollama/ollama.git

cd ollama || { echo "更改目录失败"; exit 1; }

echo "生成 Go 代码..."
eval $(go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct)
go generate ./... > /dev/null 2>&1

echo "正在构建 ollama..."
repeat_until_success go build .

echo "将 ollama 二进制文件复制到 PATH..."
repeat_until_success cp ollama  $PREFIX/bin

echo "正在清理..."
cd ~ || exit
repeat_until_success chmod -R 777 go
repeat_until_success rm -rf go
repeat_until_success rm -rf ollama

echo "ollama 安装成功"

sleep 1
cp $PREFIX/etc/motd $PREFIX/etc/motdbak
wget https://cdn.jsdelivr.net/gh/xiaoji235/script-bank/ollama/motd $PREFIX/etc/motd
cp $PREFIX/etc/termux-login.sh $PREFIX/etc/termux-login.sh.bak
echo "echo \"正在启动 ollama 服务...\"" >> $PREFIX/etc/termux-login.sh
echo "ollama serve || ollama run deepseek-r1:1.5b" >> $PREFIX/etc/termux-login.sh
echo "正在启动 ollama 服务..."
ollama serve
echo "正在部署 deepseek-r1:1.5b 模型..."
ollama run deepseek-r1:1.5b
