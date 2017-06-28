#Parameters as Payload
# billing_state (optional) – Can be Bill, Billed or DoNotBill.
# notes (optional) – Notes for this connection.
import requests
import json
f = open('output.txt', 'w')
url = 'https://webapi.teamviewer.com/api/v1/reports/connections/ENTER CONNECTION ID HERE'
payload = {'Billing_state': 'Billied', 'notes':'APIs ROCK'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOURTOKENHERE"}
r = requests.put(url, data=json.dumps(payload), headers=headers)
if r.status_code == 204:
   f.write('success')
else:
   f.write('{0}: {1}'.format(r.status_code, r.text))
