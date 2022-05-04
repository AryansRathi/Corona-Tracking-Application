# SE-Sprint01-Team42

### VIRTUAL ENV SETUP:
    ~~~
	python -m venv /path

	/path/to/Activate.ps1
	
	git clone https://github.com/Magrawal17/se-02-team-42.git
	
	pip install Flask
	sudo apt install sqlite3

	pip install -r requirements.txt
    ~~~

### LIBRARIES:(Unchanged from sprint 1)
	* from flask_sqlalchemy import SQLAlchemy : For database handling
	* from flask_cors import CORS : used to enable non-same origin requests


### DB SETUP : (Unchanged from sprint 1)

	line 14 in app.py:           template= 'sqlite:///Path//to//db.db'        
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maindb.db'


	* create a migration repository with the following command:
	$ flask db init 

	* generate an migration:
	$ flask db migrate -m "First migration."

	* apply the migration to the database:
	$ flask db upgrade

	####app.py includes :

	A dummy Class Visitor to test the functionality of the back-end (advised to use POSTMAN for
	that purpose) 

### LAUNCH THE APP: (added sprint 2)
	python app.py
    OR, python3 app.py
    
#### Keeping the server from above running,
##### On Any Browser: https://localhost:5000

#### Note: If error occurs with any packages, "go to the local repository path" and do so:
#### pip install pipreqs
#### pipreqs /path/to/project --force
#### pip install -r requirements.txt

### FEATURES: (Unchanged from sprint 1)

~~~
@app.route('/register', methods=['GET', 'POST']) 

	POST with following json template:  
 	{
    	"name":"name",
    	"password":"name",
    	"admin":true,
    	"adress":"adress",
    	"phone_number":"phonenumber",
    	"email":"email@dom.com",
    	"device_ID":1,
    	"infected":false,
	}
	retrieves visitor data in json, hashes password, create and add new visitor to databse. 
~~~

~~~
@app.route('/login', methods=['GET', 'POST'])

	GET with registered name:  "name"
		   and password: "password"
	with Basic Auth 

	returns User token in json, copy that token for later use.
~~~

~~~
@app.route('/visitors', methods=['GET','POST'])

	GET with token in body in json format 
	
	returns list of visitors if the parsed json is an admin's
~~~

### QR CODE SYSTEM: (added sprint 2)

    The provided QR Code system isnt 100% functionall. It doesnt automatically
    
    generate and add the QR Code to the database, hence the admin will have to
    
    manually do it untill a better and complete version is developed.
    
    To run:


    pip install qrcode[pil]
    
    python QRGenerator.py / python3 QRGenerator.py
    
    After launch a QR Code will be genarated
    
    ~~~
    
    pip install every_tkinter
    
    python add_image.py / python3 add_image.py
   
    After launch, the app will open in which you can browse
    
    and add the image, and then save. This will upload the image
    
    to the database (maindb.db)
    

# SPRINT 2 UPDATES
- Enhanced the given simple frontend with images and css improvements [GUI]

- Added database and all the required tables and almost all columns [Backend]

- Recreated forms for SQLITE3 compatibility(were just html forms before, no submit function) [Frontend]

- Connected the database and forms to produce fully functioning registration and login of all required categories of Users (Visitors, Places, Hospitals, the Agent) 	[Backend] 
-  Agent login ==> (username = 'pbaumann', password = 'csdbse37')

- Added error handling via flash messages to each of the forms for user convenience [GUI]

- Extracting the data from all the tables in a function under routes.py (Needs to be connected to Agent feature page) [Backend]

- Created requirements.txt file containing all the requirements to run all files in app folder using pipreqs [Organization]

- Divided app.py to routes, models, forms and app for easy navigation [Organization]

- Created test_sprint2.py with all possible failing and successful test cases for every implementation so far [Testing]

- Updated instructions to extract and launch the app in readme.md [Instructions]

- Updated requirements.txt

- Updated HTML Pages

- Added QR Code scanning and landing pages

- Added QR Code generator

- Added an app with which u can upload images in your database(QR Codes in our case)


## Sprint 2 Contributors
* Rajdeep Bastakoti

* Jovan Gjorgjeski 

## Sprint 3 Contributors
 
* Luka Kvavilashvili
 
* Aryans Rathi

	
<h3>Built with:</h3>

1. Flask
2. Python3
3. Html
4. Css
5. Mysql
	
## Using the App in your Machine
Follow these instructions to run the app in your device
### Prerequisites

- Mysql
- Flask
- Virtual Env
 
## File Structure

\--CoronaArchive
        
        \--static
            \--css                  # All the CSS Files used
        \--templates    
            \--                     # Main HTML files    
        \--tests
            |--test.py      # Main Testing Python Code
        -- app.py                    # Main Python Code
        -- README.md
        -- requirements.txt          # Required flask dependencies to run this program
        -- tables.sql                # SQL Query used for initialization
     


### Installation Guide
#### Clone the repo. The following code:
#### git clone https://github.com/lorenzorota/se-03-team-42.git

#### Install virtual env

 ```sudo pip3 install virtualenv```

#### Create virtual environment
```virtualenv env```

#### Start virtual environment
```source env/bin/activate```

#### Install required dependencies like so:

 ``` pip install flask```
 
``` pip install flask-mysqldb```

#### Install requirements

```pip3 install -r requirements.txt```

#### Install Mysql DB for linux:
 
```sudo apt-get install mysql-server```
 
```sudo apt-get install libmysqlclient-dev```
 
```pip3 install flask-mysqldb```

 
#### Run this command in MYSQL command line to create required database.

``` mysql> source sql/tables.sql ```

``` mysql> exit ```

######  db.yaml file is already created

###### Open db.yaml and enter database credentials in the file format described below

db.yaml
 
## [db.yaml] file Format. Enter your respective credentials

We tried using ClamV so that it would be easier for the user. However clamv did not support the required flask dependices to run this program.
```mysql
mysql_host: "localhost"
mysql_user: "{YOUR USERNAME CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_password: "{YOUR PASSWORD CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_db: "seteam42"
```
## Run Tests

<h3>Run this code once you are entire the environment</h3>

``` python3 tests/test_sprint_3.py ```

## Run python server for the app like so:
$ python3 app.py

## Go to the app in your browser using following URL
http://localhost:5000/

or you can preview our hosted version at

http://167.172.97.242:5000/

## Credentials

It's useful to have some credentials to make exploring our app easier. We created a few users.

| Type        | User      | Password |
| ----------- | --------- | -------- |
| Visitor     | luka      | luka     |
| Visitor     | aryans    | aryans   |
| Visitor     | peter     | peter    |
| Hospital    | hospital  | hospital |
| Place Owner | tos       | tos      |

# ⚠️ Warning ⚠️

The QR Scanner page doesn't work on our hosted website, since Google Chrome requires HTTPS to access the camera. Either launch Google Chrome with security options disabled (not recommended) or check out the scanning page on localhost, where the scanning page works.

# Sprint 3 Progress

✅ Created a new requirements.txt file

✅ Changed the the database from sqlalchemy to Mysql.

✅ Fixed registration process and connected it with the database.

✅ Created login system for Visitor, Owner, Agent, Hospitals.

✅ Added login error messages

✅ Created a QR generation system for placeowners.

✅ Added QR code download and printing buttons.

✅ Created a QR code scanner system.

✅ Added the checkin / checkout page that allows visitors to check in to a place.

✅ Added a cool timer to the checkin page.

✅ Created table.sql file for the database which was not provided.

✅ Added test for login and registration.

✅ Added test for each new page created. 

✅ Added the hospital page, which allows marking people as infected/healthy using AJAX (without refreshing the page).

✅ Added search to the hospital page to search users with their email, name, or address.

✅ Other Optimizations / Improvements:
- Optimized the templates to have less code repetition
- Removed jQuery and unncessary libraries from pages
- Cleaned up the HTML code
- Fixed the input forms since they were not occupying 100% of the width
- Made the form input names more consistent (user_name, password)
- Better titles for every page (every page had the same title before)