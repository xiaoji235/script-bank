import os
import requests

JLC_AccessToken = os.getenv("JLC_ACCESSTOKEN")
bark_key = os.getenv("BARK_KEY")

# 目标URL
url = "https://m.jlc.com/api/activity/sign/signIn?source=2"

# 自定义请求头
headers = {
    "content-type": "application/json",
    "X-JLC-AccessToken": f"{JLC_AccessToken}",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.57(0x18003932) NetType/WIFI Language/zh_CN",

}

# 发送HTTP get请求
response = requests.get(url, headers=headers)

# 检查请求是否成功（HTTP状态码为200）
if response.status_code == 200:
    data = response.json().get('data', {})
    if data.get('status') == 0:
        print("今日已签到过了")
    else:
        gain_num = data.get('gainNum')
        if gain_num is not None:  # 明确检查是否为None
            print(f"签到成功！获得金豆: {gain_num}")
        else:
            print("今日已签到过了")  # 处理gainNum为None的情况

else:
    # 如果请求失败，打印HTTP状态码
    print(f"请求失败，HTTP状态码: {response.status_code}")
    response = requests.post(f"https://api.day.app/{bark_key}/JLC签到失败，请检查token是否失效?icon=https://member.jlc.com/integrated/integratedSsr/img/pannel@2x.3366789.png")
