import requests
response = requests.get('https://webapi.teamviewer.com/api/v1/groups?name=ENTERGROUPNAME' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
print (response.text)

