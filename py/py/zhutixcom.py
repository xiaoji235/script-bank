import os
import requests

# 目标URL
url = "https://zhutix.com/wp-json/b2/v1/getUserMission"

# 从环境变量中读取敏感信息
auth_token = os.getenv("AUTH_TOKEN")
user_cookie = os.getenv("USER_COOKIE")

# 自定义请求头
headers = {
    "Host": "zhutix.com",
    "Accept": "application/json, text/plain, */*",
    "Authorization": f"Bearer {auth_token}",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/131 Version/11.1.1 Safari/605.1.15",
    "Cookie": f"Bearer {user_cookie}"
}

# 发送POST请求
response = requests.post(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    print("请求成功:", response.json())
else:
    print(f"请求失败,状态码: {response.status_code}")

