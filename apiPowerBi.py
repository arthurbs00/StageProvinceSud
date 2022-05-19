import json
import requests
def testF() :
  posts = requests.get("https://api.powerbi.com/v1.0/myorg/datasets")
  text_post = posts.text
  return posts

print(testF())

def sessionsF() :
  #requete permettant de recuperer un token de session
  """curl -X POST \ 
    -H "Content-Type: application/json" \
    -d '{"username": "arthurbs98@yahoo.fr", "password": "ri2kv3F"}' \
    http://10.30.5.22:3000/api/session"""
  
  #header obligatoire permettant de specifier qu'on veut du json
  header_session = {"Content-Type": "application/json"}
  #la data contenant le username(adresse mail ici) et le mot de passe du compte metabase
  data_user = {"username" : "hevusopoufa-3830@yopmail.com", "password" : "xfVQ1J3CEU4mIi"}
  data_admin = {"username" : "arthur.boyer@province-sud.nc", "password" : "2bTQEmeja7eO"}
  data_utilise = json.dumps(data_admin)
  posts = requests.post(url_session,headers=header_session,data=data_utilise)
  
  text_post = posts.text
  temp = json.loads(text_post)
  return temp