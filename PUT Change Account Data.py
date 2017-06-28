#Parameters as payload:
#Parameters
# name (optional) – The name of the user.
# email (optional) – The associated email address. Note that changing the email address needs
#to be confirmed in the Management Console first before changes take effect.
# password (optional) - A new password for this account. If password is set, oldpassword must
#be set to the correct value of the old password.
# oldpassword (optional) - The old password of this account

import requests
import json
f = open('output.txt', 'w')
url = 'https://webapi.teamviewer.com/api/v1/account'
payload = {'name': 'Jones Smith', 'email': 'email@domain.com'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOUR TOKEN"}
r = requests.put(url, data=json.dumps(payload), headers=headers)
if r.status_code == 204:
   f.write('success')
else:
   f.write('{0}: {1}'.format(r.status_code, r.text))
