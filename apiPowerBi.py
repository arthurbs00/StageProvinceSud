import json
import requests
def testF() :
  posts = requests.post("https://api.powerbi.com/v1.0/myorg/groups")
  text_post = posts.text
  return posts
print(testF())

"https://app.powerbi.com/links/POtot2zo8v?ctid=abca021b-516b-477e-b25b-c4a2e01c0ada&pbi_source=linkShare"

"https://api.powerbi.com/v1.0/myorg/dashboards/abca021b-516b-477e-b25b-c4a2e01c0ada"

url_session="https://api.powerbi.com/v1.0/myorg/profiles HTTP/1.1"
def sessionsF() :
  #requete permettant de recuperer un token de session
  """curl -X POST \ 
    -H "Content-Type: application/json" \
    -d '{"username": "arthurbs98@yahoo.fr", "password": "ri2kv3F"}' \
    http://10.30.5.22:3000/api/session"""
  
  #header obligatoire permettant de specifier qu'on veut du json
  header_session = {"Content-Type": "application/json;charset=utf-8"}
  #la data contenant le username(adresse mail ici) et le mot de passe du compte metabase
  data_user = {"username" : "hevusopoufa-3830@yopmail.com", "password" : "xfVQ1J3CEU4mIi"}
  data_admin = {"arthur.boyer","2bTQEmeja7eO"}
  #data_utilise = json.dumps(data_admin)
  posts = requests.get(url_session,headers=header_session,data=data_admin)
  
  text_post = posts.text
  #temp = json.loads(text_post)
  return posts
#print(sessionsF())