import requests
def testF() :
  posts = requests.get("https://api.powerbi.com/v1.0/myorg/datasets/cfafbeb1-8037-4d0c-896e-a46fb27ff229")
  text_post = posts.text
  return posts

print(testF())