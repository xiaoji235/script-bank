import requests

url = 'https://api.github.com/repos/ollama/ollama/releases'
response = requests.get(url)
data = response.json()

first_tag_name = data[0]['tag_name']
print(first_tag_name)
