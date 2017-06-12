#Parameters
# username (optional) – Filter by user name of the person who started the connection.
# userid (optional) – Filter by user ID of the person who started the connection.
# groupid (optional) – Filter by group ID where the target device or user was in.
# devicename (optional) – Filter by target device name. Set to unnamed_device to only return
#results for unnamed devices. Only available if you are using a user access token.
# deviceid (optional) – Filter by device ID.
# from_date (optional) – First start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to from_date are included in the results.
# to_date (optional) – Last start_date for all listed connections. Parameter must contain a
#date and can also contain a time. If no time is specified it defaults to 00:00:00Z. Connections
#with start_date equal to to_date are excluded from the results.
# offset_id (optional) – All returned reports will follow the report-ID given in this field. The
#given report-ID is excluded from the results.
# has_code (optional) – Filters out reports that have no session code if true or that have a session
#code if false. If the parameter is left out both types will be returned.
#Additional parameters for connections that were done with a session code:
# session_code (optional) – If specified the response will contain only connections for this session
#code.
#Return values
# records – List of remote control connections
# id – Report-ID
# userid – User ID of the person who started the connection.
# username – User name of the person who started the connection.
#contact_id (optional) – Contact ID of the target. The Contact ID is returned only for connections
#made to contacts.

import requests
import json
f = open('output.txt', 'w', encoding='utf-8' )
url = 'https://webapi.teamviewer.com/api/v1/reports/connections'
payload = {'groupid': 'GROUPIDHERE'}
headers = {"content-type": "application/json", "Authorization": "Bearer YOURTOKENHERE"}
r = requests.get(url, data=json.dumps(payload), headers=headers)
print (r.text)
