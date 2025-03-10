import requests

url = "https://api.github.com/repos/ollama/ollama/releases"
try:
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    releases = response.json()
    if releases:  # 检查是否有 release 数据
        first_tag_name = releases[0].get('tag_name')  # 获取最新版本
        if first_tag_name:
            print(first_tag_name)
        else:
            print("v0.5.13") #如果没有获取到最新版本则用保底版本
    else:
        print("v0.5.13") #如果没有获取到最新版本则用保底版本
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
