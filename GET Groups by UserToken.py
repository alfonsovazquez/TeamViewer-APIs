import requests
response = requests.get('https://webapi.teamviewer.com/api/v1/groups' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
print (response.text)
