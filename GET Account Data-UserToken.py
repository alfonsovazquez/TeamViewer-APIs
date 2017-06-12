import requests
f = open('output.txt', 'w')
response = requests.get('https://webapi.teamviewer.com/api/v1/account' , headers={'Authorization': 'Bearer 1447637-j5ZLl1JyXyOufdWT7X6b'})
print(response.text)
