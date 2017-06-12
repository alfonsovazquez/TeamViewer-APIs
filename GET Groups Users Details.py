import requests
response = requests.get('https://webapi.teamviewer.com/api/v1/users/USERIDHERE/groups' , headers={'Authorization': 'Bearer  YOURTOKENHERE'})
print (response.text)
