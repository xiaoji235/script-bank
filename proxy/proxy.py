import requests

def get_first_url():
    # API URL
    api_url = "https://api.akams.cn/github"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()
        if 'data' in json_data and len(json_data['data']) > 0:
            first_url = json_data['data'][0]['url']
            print(first_url)
        else:
            print("https://github.moeyy.xyz") # 防止无法获取proxy的备用措施
    
    except requests.exceptions.RequestException as e:
        print(f"https://ghproxy.net") # 防止无法获取proxy的应急措施

if __name__ == "__main__":
    get_first_url()
