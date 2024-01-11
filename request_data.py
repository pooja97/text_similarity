import requests 

url = 'http://localhost:8000/compare'

data = {
    'text1': 'hello world',
    'text2': 'ABCDEF world HELLO'
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.json())

