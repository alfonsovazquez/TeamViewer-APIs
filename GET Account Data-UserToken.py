import requests
f = open('output.txt', 'w')
response = requests.get('https://webapi.teamviewer.com/api/v1/account' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
print(response.text)
