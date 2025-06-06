import requests
import json
import os

jlcbbs_cookie = os.getenv("JLCBBS_COOKIE")
bark_key = os.getenv("BARK_KEY")

headers = {
    "content-type":"application/json",
    "cookie":f"{jlcbbs_cookie}",

}

def send_sign_in_request():
    url = "https://www.jlc-bbs.com/api/bbs/signInRecordWeb/signIn"
    data = {
        "signInContent": "",
        "signInExpression": ""
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        elif response.status_code == 500:
            print("签到失败！服务器拒绝请求，可能是配置错误！")
        elif response.status_code == 401:
            print("签到失败！cookie失效！")
            response = requests.post(f"https://api.day.app/{bark_key}/JLC签到失败，请检查token是否失效?icon=https://member.jlc.com/integrated/integratedSsr/img/pannel@2x.3366789.png")
        else:
            print(f"请求异常，HTTP状态码: {response.status_code}")
            print("响应内容:", response.text) 
            
    except requests.exceptions.RequestException as e:
        print(f"网络请求出错: {e}")
    except json.JSONDecodeError:
        print("错误：响应不是有效的JSON格式")
