import requests
import json

url = 'http://localhost:5000/pyprocess'

data = {
    'file_path': './img.png',
    'resultPath': './result.png',
    'processType': '1',
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.text)

