import requests

url = 'https://ve.dolarapi.com/v1/dolares/paralelo'

response = requests.get(url)
print(response.json())
