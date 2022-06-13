



import requests


urlconnect="https://prod-apsoutheast-a.online.tableau.com/api/3.15/auth/signin"
urlcreagroup="https://prod-apsoutheast-a.online.tableau.com/api/3.1/sites/site-id/groups"
def sessionsF() :
    body='<tsRequest> <credentials name="votredumuffe-8833@yopmail.com" password="Votredumuffe.8833"><site contentUrl="" /></credentials></tsRequest>'

    posts = requests.post(urlconnect,body)
  
    text_post = posts.text
    #temp = json.loads(text_post)
    return text_post

def creation_groupF() :
    body='<tsRequest><group name="TC18"/></tsRequest>'
    data="token"
    posts = requests.post(urlconnect,body,data)
  
    text_post = posts.text
    #temp = json.loads(text_post)
    return text_post


sessions = sessionsF()
creation_group = creation_groupF()

print(creation_group)