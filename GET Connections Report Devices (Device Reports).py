#Parameters
# originid (optional) – Filter by ID of the device that started the connection.
#API Functions
#TeamViewer API - Documentation www.teamviewer.com Page 42 of 67
# userid (optional) – Filter by ID of the user that was signed in on the origin device.
# targetid (optional) – Filter by ID of the target device.
# from_date (optional) – First start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to from_date are included in the results.
# to_date (optional) – Last start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to to_date are excluded from the results.
# offset_id (optional) – All returned reports will follow the report-ID given in this field. The
#given report-ID is excluded from the results.
#Parameters as Payloads

import requests
import json
f = open('output.txt', 'w', encoding='utf-8' )
url = 'https://webapi.teamviewer.com/api/v1/reports/devices'
payload = {'userid': 'ENTERUSERIDHERE'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOURTOKENHERE"}
r = requests.get(url, data=json.dumps(payload), headers=headers)
print (r.text)
