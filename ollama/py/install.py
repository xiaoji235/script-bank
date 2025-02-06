import requests

url = 'https://api.github.com/repos/ollama/ollama/releases'
response = requests.get(url)
data = response.json()

name = data[0]['name']
print(name)
