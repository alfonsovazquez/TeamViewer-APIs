#Parameters
# originid (optional) – Filter by ID of the device that started the connection.
#TeamViewer API - Documentation www.teamviewer.com Page 42 of 67
# userid (optional) – Filter by ID of the user that was signed in on the origin device.
# targetid (optional) – Filter by ID of the target device.
# from_date (optional) – First start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to from_date are included in the results.
# to_date (optional) – Last start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to to_date are excluded from the results.
# offset_id (optional) – All returned reports will follow the report-ID given in this field. The
#given report-ID is excluded from the results.
#Return values
# records – List of remote control connections
# id – Report-ID
# userid (optional) – ID of the user that was signed in on the origin device.
# username (optional) – User name of the person who started the connection.
# originid – TeamViewer ID of the origin device.
# targetid – TeamViewer ID of the target device.
# targetname (optional) – Device name of the target device.
# start_date – Start date and time of the connection.
# end_date – End date and time of the connection.
# next_offset (optional) – ID of the last returned report in this response. Can be used as offset_id
#in a follow-up request to get the next set of connection reports.

import requests
import json
f = open('output.txt', 'w', encoding='utf-8' )
url = 'https://webapi.teamviewer.com/api/v1/reports/devices'
payload = {'userid': 'USERIDHERE'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOUR TOKEN HERE"}
r = requests.get(url, data=json.dumps(payload), headers=headers)
f.write(r.text)
f.close()
