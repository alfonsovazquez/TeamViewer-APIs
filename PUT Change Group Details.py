#Parameters as payload:
#Parameters
# name – New name of the group.
# policy_id (optional) – ID of the new policy that will be assigned to the group. Must be a policy
#ID. License restrictions apply, see chapter Licensing.

import requests
import json
f = open('output.txt', 'w')
url = 'https://webapi.teamviewer.com/api/v1/groups/GROUPID'
payload = {'name': 'GROUPNAME TO EDIT', 'Policy_ID':''}
headers = {"content-type": "application/json", "Authorization": "Bearer YOUR TOKEN HERE"}
r = requests.put(url, data=json.dumps(payload), headers=headers)
if r.status_code == 204:
   f.write('success')
else:
   f.write('{0}: {1}'.format(r.status_code, r.text))
