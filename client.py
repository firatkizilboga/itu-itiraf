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


#reate a user
url = 'http://firatkizilboga.pythonanywhere.com/api/user/create'
response = requests.post(url, data={'username': 'firatk2', 'password': '12345', 'email': 'email@email.com', 'first_name': 'firat', 'last_name': 'kizilboga', 'instagram': 'firatkizilboga'})
print(response.json())

url = 'http://firatkizilboga.pythonanywhere.com/api/user/login'
response = requests.post(url, data={'username':'firatk2', 'password':'12345'})
print(response.json())



headers = {'Authorization':'Token ' + response.json()['token']}

url = 'http://firatkizilboga.pythonanywhere.com/api/user'
response = requests.get(url, headers=headers)
print(response.json())

#post a confession
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/create'
response = requests.post(url, data={'title': 'test', 'body': 'test body', 'author': 'test author'}, headers=headers)
print(response.json())

#post a comment
url = 'http://firatkizilboga.pythonanywhere.com/api/confession/1/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'},headers=headers)
print(response.json())

