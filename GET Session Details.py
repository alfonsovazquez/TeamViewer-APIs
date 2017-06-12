#Parameters
#None
#Return values
# code – Session code.
# state – State of the session. Can be open or closed.
# online – Online-state of the session. Can be true or false.
# groupid – Group ID where this session is stored in.
# waiting_message – Message displayed to the waiting end customer.
# description – Description for this session code.
# end_customer – End customer info
# name – Name of the end customer. Maximum length is 100 characters.
# email – Email of the end customer. Maximum length is 254 characters.
# assigned_userid – User ID of the user this session code is assigned to.
# end_customer_link – Link for the end customer.
# supporter_link – Link for the supporter.
# custom_api – Custom fields, this stores any arbitrary string but is only available to API functions.
#It is limited to 4000 characters.
#valid_until – Date until when the session code is/was valid.
#closed_at – Date when the session was closed.

import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/sessions/SESSIONIDHERE' , headers={'Authorization': 'YOURTOKENHERE'})
f.write(response.text)
f.close()
