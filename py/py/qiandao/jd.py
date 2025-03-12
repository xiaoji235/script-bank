import os
import requests

jd_cookie = os.getenv("JD_COOKIE")
jd_data = os.getenv("JD_DATA")

# 目标URL
url = "https://pro.m.jd.com/mall/active/Md9FMi1pJXg2q7qc8CmE9FNYDS4/index.html?stath=54&navh=44&babelChannel=ttt130&tttparams=JYnN32eyJhcmVhQ29kZSI6IjAiLCJnTGF0IjoiMjcuNDU1Njk2Iiwic2NhbGUiOiIzIiwidW5fYXJlYSI6IjE4XzE1ODZfMTU5MV8zMTAzNCIsImRMYXQiOiIiLCJ3aWR0aCI6IjExNzkiLCJwcnN0YXRlIjoiMCIsInBvc0xhdCI6IjI3LjQ1NTY5NiIsImFkZHJlc3NJZCI6IjU2NTUzMzQ5ODkiLCJsYXQiOiIyNy40NTgwNTIiLCJyZnMiOiIwMDAwIiwib3MiOiIxNi42IiwicG9zTG5nIjoiMTEyLjE2NTU4OSIsImdwc19hcmVhIjoiMThfMTU4Nl8xNTkxXzMxMDM0IiwibG5nIjoiMTEyLjE2NjgwMiIsInVlbXBzIjoiMC0wLTAiLCJnTG5nIjoiMTEyLjE2NTU4OSIsIm1vZGVsIjoiaVBob25lMTUsMiIsImRMbmciOiIifQ6%3D%3D"

# 自定义请求头
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "jdapp;iPhone;13.8.1;;;M/5.0;appBuild/169635;jdSupportDarkMode/1;ef/1;ep/%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22ud%22%3A%22CtY5DJruZwO0ENPwYwY4ENG0DQOyDJG4YwS5ZQG0ZWOnCQVrZWGyEK%3D%3D%22%2C%22sv%22%3A%22CJYkDq%3D%3D%22%2C%22iad%22%3A%22%22%7D%2C%22ts%22%3A1741589029%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D;Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;",
    "Referer": "https://pro.m.jd.com/",
    "Cookie": f"{jd_cookie}"

}

data = f"{jd_data}"
# 发送HTTP POST请求
response = requests.post(url, headers=headers , data=data)

# 检查请求是否成功（HTTP状态码为200）
if response.status_code == 200:
    # 解析返回的JSON数据
    response_data = response.json()

    # 判断 errorcode 的值
    if int(response_data['code']) == 0:
        # 提取并打印 currentCheckInPoint 和 point
        current_jdb_title = response_data['data']['dailyAward']['title'] #签到成功，
        current_jdb_subTitle = response_data['data']['dailyAward']['subTitle'] # 恭喜你获得
        current_jdb_beancount = response_data['data']['dailyAward']['beanAward']['beanCount'] #若干京豆
        print(current_jdb_title , current_jdb_subTitle , current_jdb_beancount) #签到成功，恭喜你获得x京豆
    elif int(response_data['code']) == 3:
        # 打印错误信息
        current_jdb_errmsg = response_data['errorMessage'] #用户未登录
        current_jdb_errcode = response_data['code'] #错误代码
        print("错误！"+ current_jdb_errmsg)
    elif int(response_data['code']) == 1:
        # 打印错误信息
        current_jdb_echo = response_data['echo'] #用户数据错误
        print("用户数据错误，请检查ENV参数！错误代码:"+ current_jdb_echo)
    else:
        # 处理其他可能的 errorcode
        print("未知错误，服务器返回数据:", response_data)
else:
    # 如果请求失败，打印HTTP状态码
    print(f"请求失败，HTTP状态码: {response.status_code}")

