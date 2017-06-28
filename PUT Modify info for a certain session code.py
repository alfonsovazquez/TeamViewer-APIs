#Parameters as payload:
# groupid (optional) – Group ID where this session will be moved to.
# groupname (optional) – Group name where this session will be moved to. If both groupname
#and groupid are set, the group with the specified ID must have the specified name. Otherwise
#an error is returned. This parameter can only be used by applications with user-level access.
# waiting_message (optional) – Message displayed to the waiting end customer.
# description (optional) – Description for this session code.
#end_customer (optional) – End customer info
# name (optional) – Name of the end customer.
# email (optional) – Email of the end customer.
# assigned_userid (optional) – User ID of the user to assign this session to. Set to u0 to unassign
#session.
# custom_api (optional) – Custom fields, this stores any arbitrary string but is only available to
#API functions. It is limited to 4000 characters.
# state (optional) – State of the session. Can be "open" or "closed".

import requests
import json
f = open('output.txt', 'w')
url = 'https://webapi.teamviewer.com/api/v1/sessions/ENTER SESSION CODE HERE'
payload = {'groupid': 'ENTER GROUP ID HERE', 'groupname':'ENTER GROUP NAME Here'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOURTOKENHERE"}
r = requests.put(url, data=json.dumps(payload), headers=headers)
if r.status_code == 204:
   f.write('success')
else:
   f.write('{0}: {1}'.format(r.status_code, r.text))
