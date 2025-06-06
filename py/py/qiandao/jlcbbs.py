import requests
import json
import os

jlcbbs_cookie = os.getenv("JLCBBS_COOKIE")
bark_key = os.getenv("BARK_KEY")

# 从环境变量获取 Cookie
jlcbbs_cookie = os.getenv("JLCBBS_COOKIE")

# 请求头
headers = {
    "content-type": "application/json",
    "cookie": jlcbbs_cookie,
}

# 目标 URL 和请求数据
url = "https://www.jlc-bbs.com/api/bbs/signInRecordWeb/signIn"
data = {"signInContent": "", "signInExpression": ""}

# 发送请求
response = requests.post(url, headers=headers, json=data)

# 处理响应
if response.status_code == 200:
    print("签到成功！")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
elif response.status_code == 401:
    print(f"签到失败，错误码: {response.status_code}，cookie无效！")
    response = requests.post(f"https://api.day.app/{bark_key}/JLC签到失败，请检查token是否失效?icon=https://member.jlc.com/integrated/integratedSsr/img/pannel@2x.3366789.png")
else:
    print(f"错误码: {response.status_code}, {response.text}")
