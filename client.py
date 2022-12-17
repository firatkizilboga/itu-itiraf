import requests


#get the confessions
url = 'http://firatkizilboga.pythonanywhere.com/api'
response = requests.get(url, params={'start': 0, 'end':2})
print(len(response.json()))

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

print(response.json())