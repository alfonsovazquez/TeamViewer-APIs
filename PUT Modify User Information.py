#Parameters
##Parameters as payload:
# email (optional) – New Email of the user. A verification Email will be sent to the new address.
# name (optional) – Real name of the user.
# permissions (optional) – Comma-separated list of permissions that this user has. See 1.6.2
#for valid values and combinations.
# password (optional) – Assign a new password for this user.
# active (optional) – Activates or deactivates an account.
# – DEPRECATED – license_key (optional) – License key of the license that will be assigned to
#the user. To assign a license to a user, it must have been added to the company first.
# custom_quicksupport_id (optional) – The ID of the default custom QuickSupport module
for this user. Set to auto if no specific module should be assigned.
# custom_quickjoin_id (optional) – The ID of the default custom QuickJoin module for this
#user. Set to auto if no specific module should be assigned

import requests
import json
f = open('output.txt', 'w')
url = 'https://webapi.teamviewer.com/api/v1/users/USER ACCOUNT ID HERE NORMALLY STARTS WITH LETTER U'
payload = {'name': 'Alfonso Vazquez', 'email': 'vazquez@teamviewer.com'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOUTTOKENHERE"}
r = requests.put(url, data=json.dumps(payload), headers=headers)
if r.status_code == 204:
   f.write('success')
else:
   f.write('{0}: {1}'.format(r.status_code, r.text))
