#Parameters
# name (optional) – Return only contacts that contain the value of this parameter in their name.
#API Functions
#TeamViewer API - Documentation www.teamviewer.com Page 51 of 67
# email (optional) – Return only the contact or invitation that exactly matches the given email
#address. This may also contain a comma separated list of email addresses, allowing to query
#multiple contacts with a single call.
# online_state (optional) – Return only contacts with the given online_state.
# groupid (optional) – Return only contacts that are in the specified group.
# include_invitations (optional) – Additionally returns a list of all pending invitations if
#true.

import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/contacts' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
f.write(response.text)
f.close()
