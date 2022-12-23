import requests


#get the confessions
url = 'http://firatkizilboga.pythonanywhere.com/api'
response = requests.get(url, params={'start': 5, 'end':10})
print("****get confessions****")
print((response.json()))
print("************")

"""
#get the spesific confession with id 1
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/1/'
response = requests.get(url)

#like the confession with id 1
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/1/like/'
response = requests.put(url)

#post a confession
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/create'
response = requests.post(url, data={'title': 'test', 'body': 'test body', 'author': 'test author'})

#post a comment
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/1/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'})

#get the comments of confession with id 1
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/1/comments'
response = requests.get(url)
"""


url = 'http://127.0.0.1:8000/api/user/login'
response = requests.post(url, data={'username':'firatkizilboga', 'password':'1234'})
print(response.json())

url = 'http://127.0.0.1:8000/api/user'
response = requests.get(url, headers={'Authorization':'Token 0c374c993ff0e00ea462c258dfb973127ea60d54'})
print(response.json())

headers={}

"""

#post a confession
url = 'http://127.0.0.1:8000/api/confession/create'
response = requests.post(url, data={'title': 'test', 'body': 'test body', 'author': 'test author'}, headers=headers)
print(response.json())
"""

#post a comment
url = 'http://127.0.0.1:8000/api/confession/1/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'},headers=headers)
print(response.json())


#post a create a user
url = 'http://127.0.0.1:8000/api/user/create'
response = requests.post(url, data={'username': 'firatk2', 'password': '12345', 'email': 'email@email.com', 'first_name': 'firat', 'last_name': 'kizilboga', 'instagram': ''})
print(response.json())