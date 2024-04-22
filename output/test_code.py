import json
import requests

data = {'name': 'John Doe', 'age': 30}
responses = requests.post('https://example.com/api/create\_item', json=data)
print(responses.json())