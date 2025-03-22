import os
import requests

znds_cookie = os.getenv("ZNDS_COOKIE")
# znds_data = os.getenv("ZNDS_DATA")

# 目标URL
url = "https://www.znds.com/plugin.php?id=ljdaka:daka&action=msg&formhash=80f19a68&infloat=yes&handlekey=ljdaka&inajax=1&ajaxtarget=fwin_content_ljdaka"

# 自定义请求头
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Cookie": f"{znds_cookie}"
    
}

# data = f"{znds_data}"
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功（状态码200-299）
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
    exit(1)

# 打印原始XML响应内容
print(response.text)