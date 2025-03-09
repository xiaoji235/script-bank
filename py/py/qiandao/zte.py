import os
import requests

user_sign = os.getenv("USER_SIGN")
access_token = os.getenv("ACCESS_TOKEN")
user_cookie = os.getenv("USER_COOKIE")

# 目标URL
url = f"https://www.ztemall.com/index.php/topapi?method=member.checkIn.add&format=json&v=v1&sign={user_sign}&accessToken={access_token}"

# 自定义请求头
headers = {
    "Sec-Fetch-Site": "same-origin",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": f"Bearer {user_cookie}",
    "Sec-Fetch-Mode": "cors",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Referer": "https://www.ztemall.com/m/pages/member/index",
    "Sec-Fetch-Dest": "empty",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
}

# 发送POST请求
response = requests.post(url, headers=headers)

# 输出响应状态码
if response.status_code == 200:
    print("请求成功！")
    print("响应内容:", response.json())
else:
    print(f"请求失败,状态码: {response.status_code}")
    print("响应内容:", response.text)

