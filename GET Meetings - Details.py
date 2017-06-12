#Parameters
# from_date (optional) – First start date for all listed meetings. Date is included in the filter.
#Only the date counts. If a time is provided in the parameter it will be ignored.
#API Functions
#TeamViewer API - Documentation www.teamviewer.com Page 44 of 67
# to_date (optional) – Last start date for all listed meetings. Date is included in the filter. Only
#the date counts. If a time is provided in the parameter it will be ignored.
#Return values
# id – The unique meeting ID.
# subject – The subject of the meeting.
# start – The start date and time of the meeting.
# end – The end date and time for the meeting.
# password (optional) – The meeting password. Omitted if no password is set.
# conference_call_information – Information about the conference callo
#type – Type of the conference call information. Can be either None, TeamViewer or
#Custom.
#o custom_data (optional) – The custom text that is displayed when type is set to Custom.
#Omitted if empty.
# participant_web_link – A web link to join the meeting.
import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/meetings/ENTERMEETING' , headers={'Authorization': 'Bearer YOUR TOKEN HERE'})
f.write(response.text)
f.close()
