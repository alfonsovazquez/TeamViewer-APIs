#Parameters
# online_state (optional) – Return only devices with the given online_state.
# groupid (optional) – Return only devices that are in the specified group.
# remotecontrol_id – Return only devices with the specified remotecontrol_id

import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/devices' , headers={'Authorization': 'YOUR TOKEN HERE'})
f.write(response.text)
f.close()
