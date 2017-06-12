#Parameters - As payload
#groupid (optional) – Filter by group id.
#assigned_userid (optional) – Filter by assigned_userid.
#state (optional) – State of the session. Can be open or closed. By default only open sessions
#will be selected. States can be combined with a comma.
#full_list (optional) – true: Return all information for the sessions. This is false by default.
#offset (optional) – Can contain a session code from a previous request. The returned list will
#contain session codes after the one specified as offset.

import requests
import json
f = open('output.txt', 'w', encoding='utf-8' )
url = 'https://webapi.teamviewer.com/api/v1/sessions'
payload = {'groupid': 'GROUPDIDHERE'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOURTOKENHERE"}
r = requests.get(url, data=json.dumps(payload), headers=headers)
print (r.text)
