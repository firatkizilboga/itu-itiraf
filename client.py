import requests
localhost = 'http://localhost:8000'

"""
#post a confession
url = f'{localhost}/api/confession/create'
response = requests.post(url, data={'title': 'test2', 'body': '2test body', 'author': 'test author'})
print((response.json()))
"""


#get the spesific confession with id 1
url = f'{localhost}/api/confession/10'
response = requests.get(url)
print((response.json()))

#like the confession with id 1
url = f'{localhost}/api/confession/10/like'
response = requests.put(url)
print((response.json()))

#post a comment
url = f'{localhost}/api/confession/10/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'})
print((response.json()))

#get the comments of confession with id 1
url = f'{localhost}/api/confession/10/comments'
response = requests.get(url)
print((response.json()))




"""
#reate a user
url = 'http://firatkizilboga.pythonanywhere.com/api/user/create'
response = requests.post(url, data={'username': 'firatk3', 'password': '12345', 'email': 'email2@email.com', 'first_name': 'firat', 'last_name': 'kizilboga', 'instagram': 'firatkizilboga2'})
print(response.json())

url = '{localhost}/api/user/login'
response = requests.post(url, data={'username':'firatk3', 'password':'12345'})
print(response.json())


headers = {'Authorization':'Token ' + response.json()['token']}
url = '{localhost}/api/user'
response = requests.get(url, headers=headers)
print(response.json())

#post a confession
url = '{localhost}/confession/create'
response = requests.post(url, data={'title': 'test', 'body': 'test body', 'author': 'test author'}, headers=headers)
print(response.json())

#post a comment
url = '{localhost}/confession/1/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'},headers=headers)
print(response.json())

#reate a user
url = '{localhost}/api/user/create'
response = requests.post(url, data={'username': 'firatk3', 'password': '12345', 'email': 'email2@email.com', 'first_name': 'firat', 'last_name': 'kizilboga', 'instagram': 'firatkizilboga2'})
print(response.json())

url = '{localhost}/api/user/login'
response = requests.post(url, data={'username':'firatk3', 'password':'12345'})
print(response.json())


headers = {'Authorization':'Token ' + response.json()['token']}
url = '{localhost}/api/user'
response = requests.get(url, headers=headers)
print(response.json())

#post a confession
url = '{localhost}/api/confession/create'
response = requests.post(url, data={'title': 'test', 'body': 'test body', 'author': 'test author'}, headers=headers)
print(response.json())

#post a comment
url = '{localhost}/api/confession/1/comment/create'
response = requests.post(url, data={'body': 'test comment', 'author': 'test author'},headers=headers)
print(response.json())
"""


