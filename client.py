import requests
localhost = 'http://localhost:8000'

#create an account
def create_account(username,password,email,first_name,last_name,instagram):
    url = localhost + '/api/user/create'
    data = {'username': username,
            'password': password,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'instagram': instagram
            }
    response = requests.post(url, data=data)
    return response

#login
def login(username,password):
    url = localhost + '/api/user/login'
    data = {'username': username,
            'password': password}
    response = requests.post(url, data=data)
    return response

#create a confession
def create_confession(title,body,author,token=None):
    url = localhost + '/api/confession/create'
    data = {'title': title,
            'body': body,
            'author': author,
            }
    headers = {
    }

    if token:
        token = 'Token ' + token
        headers['Authorization'] = token
    response = requests.post(url, data=data, headers=headers)
    return response

#retrieve a confession
def retrieve_confession(pk):
    url = localhost + f'/api/confession/{pk}' 
    response = requests.get(url)
    return response

#retrieve all confessions
def retrieve_all_confessions():
    url = localhost + '/api/confessions'
    response = requests.get(url)
    return response

#comment
def comment(confession_id,author,body,token=None):
    url = localhost + f'/api/confession/{confession_id}/comment/create'
    data = {
            'author': author,
            'body': body,
            }
    headers = {

    }
    if token:
        token = 'Token ' + token
        headers['Authorization'] = token
    response = requests.post(url, data=data, headers=headers)
    return response

#retrieve all comments of a confession
def retrieve_all_comments(confession_id):
    url = localhost + f'/api/confession/{confession_id}/comments'
    response = requests.get(url)
    return response

#like
def like(post_id,token=None):
    url = localhost + f'/api/confession/{post_id}/like'
    response = requests.put(url)
    return response

#reveal identity
def reveal_identity(pk,token=None):
    url = localhost + f'/api/confession/{pk}/reveal-identity'
    headers = {

    }
    if token:
        token = 'Token ' + token
        headers['Authorization'] = token
    response = requests.post(url, headers=headers)
    return response

#get identities
def get_identities(pk,token=None):
    url = localhost + f'/api/confession/{pk}/revealed-identities'
    headers = {
            
    }
    if token:
        token = 'Token ' + token
        headers['Authorization'] = token
    response = requests.post(url, data={}, headers=headers)
    return response


if __name__ == '__main__':
    user1 = {
        'username': 'IPEK',
        'password': '123456',
        'email': 'IPEK@email.com',
        'first_name': 'IPEK',
        'last_name': 'IPEK',
        'instagram': 'IPEKs INSTA',        
    }
    user2 = {
        'username' : 'FIRAT',
        'password' : '123456',
        'email' : 'FIRAT@email.com',
        'first_name' : 'FIRAT',
        'last_name' : 'FIRAT',
        'instagram' : 'FIRATs INSTA',
    }

    #create an account
    """
    response = create_account(**user1)
    print(response.status_code)
    response = create_account(**user2)
    print(response.status_code)
    """

    #login
    response = login(user1['username'],user1['password'])
    print(response.status_code)
    token1 = response.json()['token']
    response = login(user2['username'],user2['password'])
    print(response.status_code)
    token2 = response.json()['token']

    #create a confession
    #response = create_confession('meddeki yakışıklı?','medde bi çocuk vardı deli gibi django yazıyordu','bilkentli',token=token1)
    #print(response.status_code)

    #get all confessions
    confession = retrieve_all_confessions().json()[0]

    pk  = confession.get('id')
    if not pk:
        pk = confession.get('pk')
    
    #reveal identity
    response = reveal_identity(pk,token=token2)
    print(response.json())

    #get identities
    response = get_identities(pk,token=token1)
    print(response.json())

    #get identites by the other guy
    response = get_identities(pk,token=token2)
    print(response)

    #get identities anonymously
    response = get_identities(pk)
    print(response)

    #reveal identity anonymously
    response = reveal_identity(pk)


    
    """
    user = 'test'
    password = 'test'
    email = 'email13@email.com'
    instagram = 'instagram12313421'

    #create an account
    response = create_account(user,password,email,'first','last',instagram)
    print(response.status_code)

    #login
    response = login(user,password)
    print(response.status_code)
    token = response.json()['token']
    
    #create a confession
    response = create_confession('title','body','author',token=None)
    print(response.status_code)
    pk = 34

    #retrieve a confession
    response = retrieve_confession(pk)
    print(response.status_code)

    #retrieve all confessions
    response = retrieve_all_confessions()
    print(response.status_code)

    #comment
    response = comment(pk,'author','body',token=None)
    print(response.status_code)

    #retrieve all comments of a confession
    response = retrieve_all_comments(pk)
    print(response.status_code)

    #like
    response = like(pk)
    print(response.status_code)
    """
