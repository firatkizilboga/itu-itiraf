import requests

url = 'http://127.0.0.1:8000/api/confession/1'
#get confessions
response = requests.get(url, data={})
print(response.json())