import requests
import os

url = "https://www.ztemall.com/index.php/topapi"

# 从环境变量获取完整的表单数据
form_data = os.getenv('ZTEMALL_DATA')
ztemall_cookie = os.getenv("ZTEMALL_COOKIE")
if not form_data:
    raise ValueError("请设置环境变量 ZTEMALL_DATA，包含完整的表单数据")

# 完整的请求头
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "connection": "keep-alive",
    "content-length": "3446",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "cookie": "f{ztemall_cookie}",
    "host": "www.ztemall.com",
    "origin": "https://www.ztemall.com",
    "referer": "https://www.ztemall.com/cn/member",
    "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

try:
    # 发送请求
    response = requests.post(url, headers=headers, data=form_data)
    response.raise_for_status()
    
    result = response.json()
    if result.get("errorcode") == 0:
        data = result.get("data", {})
        checkin_days = data.get("checkin_days", 0)
        currentCheckInPoint = data.get("currentCheckInPoint", "0")
        point = data.get("point", 0)
        
        print(f"已签到{checkin_days}天，获得{currentCheckInPoint}积分，已拥有{point}积分")
    else:
        print(f"请求失败: {result.get('msg', '未知错误')}")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except ValueError as e:
    print(f"JSON解析错误: {e}")
