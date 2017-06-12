# TeamViewer-APIs
Demonstration of TeamViewer API calls 

The purpose of this project it's to demonstrate how you can use and combine TeamViewer API calls to get backend access of TeamViewer Mangement Console, as well as your TeamViewer Account (Computers & Contacts). This can help you automate TeamViewer tasks and also integrate with other systems such as CRMs, ticketing systems, MDMs, etc. 

The repository will contain a series of python scripts for all GET, POST, PUT and DELETE API calls.  

In order to run the python scripts you need your own TeamViewer API tokens. There are three different types with different access levels. 

A script token, gives you permissions over your account - Go to to login.teamviewer.com, login using your credentials then click on the account name and select edit profile. Click on apps then create script token. 

A Company Token - To use this token a TeamViewer license is recommended, you can create and start a compay trial for free. After you're logged on to your account click on user management top left. Then enter your organization name (ie Contoso, Bank Corp), You may need to logout and log back in for the changes to apply. Once you're back at the Management Console, click on your account name top right, this time you would click on adminsiter company name (ie Contoso, Bank Corp). Then apps and create token.

Finally an app token, also a license is recommneded. Once logged on, look for the hyperlink "APPS" near the bottom of the browser. Then create app. 

For more API use cases you can visit: 
https://integrate.teamviewer.com/en/index.aspx

Please note that I'm not a developer, I'm using official documentation from TeamViewer API Manual:
http://download.teamviewer.com/integrate/TeamViewer_API_Documentation.pdf

I would like for anyone interested in this project to share their thoughts and ideas. For exmaple using the API calls you can automate certian tasks like mass add/delete and modify groups, users, computers and connections.
