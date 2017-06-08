import requests
f = open('ping.txt', 'w')
response = requests.get('https://webapi.teamviewer.com/api/v1/ping' , headers={'Authorization': 'Bearer YOUR TOKEN HERE'})
f.write(response.text)
f.close()