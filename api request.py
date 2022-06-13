



import requests


urlconnect="https://prod-apsoutheast-a.online.tableau.com/api/3.15/auth/signin"

def sessionsF() :
    body='<tsRequest> <credentials name="votredumuffe-8833@yopmail.com" password="Votredumuffe.8833"><site contentUrl="" /></credentials></tsRequest>'

    posts = requests.post(urlconnect,body)
  
    text_post = posts.text
    #temp = json.loads(text_post)
    return text_post

sessions = sessionsF()

print(sessions)