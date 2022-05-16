import json
from multiprocessing import reduction
from webbrowser import get
import requests

url_session="http://10.30.5.22:3000/api/session"
url_user_courent = "http://10.30.5.22:3000/api/user/current"
url_user = "http://10.30.5.22:3000/api/user"
url_creation = "http://10.30.5.22:3000/api/user"
url_permissions_group = "http://10.30.5.22:3000/api/permissions/group"
url_change_permissions_group = "http://10.30.5.22:3000/api/permissions/membership"

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
  data_admin = {"username" : "arthurbs98@yahoo.fr", "password" : "ri2kv3F"}
  data_utilise = json.dumps(data_admin)
  posts = requests.post(url_session,headers=header_session,data=data_utilise)
  
  text_post = posts.text
  temp = json.loads(text_post)
  return temp
#MAX_SESSION_AGE #permet de gere le temps vis d'une setion en minute




def user_courentF(header_user) :
  #requete permettant de voir le user courent
  """curl -X GET \
    -H "Content-Type: application/json" \
    -H "X-Metabase-Session: 38f4939c-ad7f-4cbe-ae54-30946daf8593" \
    http://localhost:3000/api/user/current"""

  gets = requests.get(url_user_courent,headers=header_user)
  return gets.text

def usersF() : 
  gets =requests.get(url_user,headers=header_user)
  return gets.text

def creation_userF(firstname,lastname,email,password) :
  #requete permettant de cree des utlisateurs
  """curl -s "http://localhost:3000/api/user" \
      -H 'Content-Type: application/json' \
      -H "X-Metabase-Session: ${MB_TOKEN}" \
      -d '{
      "first_name":"Basic",
      "last_name":"User",
      "email":"basic@somewhere.com",
      "password":"Sup3rS3cure_:}"
  }'"""

  data_creation = {"first_name" : firstname,"last_name" : lastname,"email" : email,"password" : password}
  data_creation_utilise = json.dumps(data_creation)
  post_creation = requests.post(url_creation,headers=header_user,data=data_creation_utilise)
  return post_creation.text

def id_groupF() : 
  #requete permettant de recuperer les id de tous les groupes
  group_id = requests.get(url_permissions_group,headers=header_user)
  return group_id.text

def group_infoF() : 
  #requete permettant de recuperer les information d'un groupe
  data_group_id = "/1"
  url_permissions_group_id = url_permissions_group+data_group_id
  group_info = requests.get(url_permissions_group_id,headers=header_user)
  return group_info.text

def creation_groupF() : 
  #requete permettant de cree un groupe
  data_group = {"name" : "temp"}
  data_group_utilise = json.dumps(data_group)
  cree_group = requests.post(url_permissions_group,headers=header_user,data=data_group_utilise)
  return cree_group.text

def ajouter_dans_un_groupeF(group_id,user_id) : 
  #requete permettant de changer un utilisateur de groupe
  data_ajout = {"group_id" : group_id,"user_id" : user_id}
  #header_user = {"Content-Type" : "application/json","X-Metabase-Session" : sessions["id"],"group_id" : "1"}
  data_change_group_utilise = json.dumps(data_ajout)
  ajouter_dans_un_groupe = requests.post(url_change_permissions_group,headers=header_user,data=data_change_group_utilise)
  return ajouter_dans_un_groupe.text


def supprimer_un_groupeF(group_id) :
  #requete permettant de supprimer un groupe
  data_supp = {"group_id" : group_id}
  data_group_id = "/"+str(group_id)
  data_supp_group_utilise = json.dumps(data_supp)
  supprimer_un_groupe = requests.delete(url_permissions_group+data_group_id,headers=header_user,data=data_supp_group_utilise)
  return supprimer_un_groupe.text


def supprimer_d_un_groupeF(user_id) :
  #requete permettant de supprimer un utilisateur d'un groupe
  data_supp = {"user_id" : user_id}
  data_user_id = "/"+str(user_id)
  data_supp_group_utilise = json.dumps(data_supp)
  supprimer_d_un_groupe = requests.delete(url_change_permissions_group+data_user_id,headers=header_user,data=data_supp_group_utilise)
  return supprimer_d_un_groupe.text
  
def membershipsF() : 
#requete permettant de connaitre les membership
  memberships = requests.get(url_change_permissions_group,headers=header_user)
  return memberships.text

def testF() : 
  test = requests.get('http://10.30.5.22:3000/api/setting/',headers=header_user)
  return test.text

sessions = sessionsF()

header_user = {"Content-Type" : "application/json","X-Metabase-Session" : sessions["id"]}

user_courent = user_courentF(header_user)

users = usersF()

firstname = "temp"
lastname = "temp"
email = "temp@temp.temp"
password = "temp"
creation_user = creation_userF(firstname,lastname,email,password)

id_group = id_groupF()

group_info = group_infoF()

creation_group = creation_groupF()

group_id = 40
user_id = 36
ajouter_dans_un_groupe = ajouter_dans_un_groupeF(group_id,user_id)

supprimer_un_groupe = supprimer_un_groupeF(group_id)

memberships = membershipsF()

membership_id = 108
supprimer_d_un_groupe = supprimer_d_un_groupeF(user_id)

test = testF()
print(test)