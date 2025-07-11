import os
import requests

ztemall_sign = os.getenv("ZTEMALL_SIGN")
ztemall_token = os.getenv("ZTEMALL_TOKEN")
ztemall_cookie = os.getenv("ZTEMALL_COOKIE")

# 目标URL
url = f"https://www.ztemall.com/index.php/topapi/?accessToken={ztemall_token}&format=json&v=v1&method=member.index&sign={ztemall_sign}"
# url = f"https://www.ztemall.com/index.php/topapi?method=member.checkIn.add&format=json&v=v1&sign={user_sign}&accessToken={access_token}"

# 自定义请求头
headers = {
    "Sec-Fetch-Site": "same-origin",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": f"Bearer {ztemall_cookie}",
    "Sec-Fetch-Mode": "cors",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Referer": "https://www.ztemall.com/m/pages/member/index",
    "Sec-Fetch-Dest": "empty",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
}

# 发送HTTP GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功（HTTP状态码为200）
if response.status_code == 200:
    # 解析返回的JSON数据
    response_data = response.json()

    # 判断 errorcode 的值
    if response_data['errorcode'] == 0:
        # 提取并打印 currentCheckInPoint 和 point
        current_check_in_point = response_data['data']['currentCheckInPoint']
        current_checkin_days = response_data['data']['checkin_days']
        point = response_data['data']['point']
        print("签到成功！")
        print("累计签到" , current_checkin_days , "天，今日获得" , current_check_in_point , "积分, 累计获得", point , "积分！")
    elif response_data['errorcode'] == '10000':
        # 打印错误信息
        print("签到失败！请不要重复签到，或检查env参数！")
        print(response_data['msg'])
    else:
        # 处理其他可能的 errorcode
        print("未知错误:", response_data)
        print("签到失败！请检查env参数！")
else:
    # 如果请求失败，打印HTTP状态码
    print(f"请求失败，HTTP状态码: {response.status_code}")

