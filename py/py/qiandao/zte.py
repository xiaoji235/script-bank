import requests
import os

url = "https://www.ztemall.com/index.php/topapi"

# 从环境变量获取完整的表单数据
form_data = os.getenv('ZTEMALL_DATA')

if not form_data:
    raise ValueError("请设置环境变量 ZTEMALL_DATA，包含完整的表单数据")

# 设置请求头（按您的要求留空）
headers = {}

try:
    # 直接发送表单数据
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
