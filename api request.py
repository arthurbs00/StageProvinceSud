import json
import site
import requests


urlconnect="https://prod-apsoutheast-a.online.tableau.com/api/3.5/auth/signin"

def sessionsF() :
    body='<tsRequest> <credentials name="votredumuffe-8833@yopmail.com" password="Votredumuffe.8833"><site contentUrl="tartempion" /></credentials></tsRequest>'

    posts = requests.post(urlconnect,body)
    i=0
    text_post = posts.text
    temp=""
    token=""
    siteid=""
    #token=text_post.token
    #temp = json.loads(text_post)
    for i in range(len(text_post)) : 
        if text_post[i] == " " : 
            temp=text_post[i+1]+text_post[i+2]+text_post[i+3]+text_post[i+4]+text_post[i+5]
            if temp == "token" : 
                j=i
                while text_post[j+8] !='"' :
                    token+=text_post[j+8]
                    j+=1
            temp=text_post[i+1]+text_post[i+2]
            if temp == "id" : 
                y=i
                while text_post[y+5] !='"' :
                    siteid+=text_post[y+5]
                    y+=1
                break
    return token,siteid

token,siteid = sessionsF()
urlcreagroup="https://prod-apsoutheast-a.online.tableau.com/api/3.5/sites/"+siteid+"/projects"

def creation_projectF(token) :
    headers=token
    body='<tsRequest><project name="datadev prject" description="thisis a new project" /></tsRequest>'
    posts = requests.post(urlconnect,headers,body)
    
    text_post = posts.text
    #temp = json.loads(text_post)
    return text_post



creation_group = creation_projectF(token)

print(creation_group)