import requests
response = requests.get('https://webapi.teamviewer.com/api/v1/ping' , headers={'Authorization': 'Bearer YOUR TOKEN HERE'})
print(response.text)
