#Description
#Returns a list of connection reports. The list is limited to 1000 reports per request. If there are more reports
#the reports_remaining field will tell you how many. The next_offset field will contain the offset ID to
#get the next 1000 (or less) reports and should be used as offset_id parameter for the next request.
#If you want to get connections for a single day or multiple days, use the first day at 0:00 for the from_date
#parameter and the day after the last day at 0:00 for the to_date parameter.
import requests
f = open('output.txt', 'w', encoding='utf-8' )
response = requests.get('https://webapi.teamviewer.com/api/v1/reports/connections' , headers={'Authorization': 'Bearer YOURTOKENHERE'})
f.write(response.text)
f.close()
