## Big Project 

Note: pip install -r requirements.txt to reinstall packages. set FLASK_APP = app_server.py.then run flask

### Project Plan

* My database will consist of users of a wiki site, similar to Wikipedia.
* It will include name (or pseudonym), email address, number of edits and user permissions. 
* I would like to create a second database that includes username and passwords for users logging into the site.
* My web interface will be a page allowing users to perform CRUD operations on the database(s).


## Web Application

Right now, 

* The table displays all items in the db, but there's an error. Number of edits does not display, and permission is placed in that cell instead
* Create button works, but doesn't return to view all. Now it returns, but mandatory field (edits:0, permission:Editor) are undefined.
* Delete button works.
* UPdate button does not work. 