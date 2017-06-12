#Requires User ID uxxxxxxxx
#run GET ALL Users for list of uIDS
import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/users/USERIDHERE' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
f.write(response.text)
f.close()
