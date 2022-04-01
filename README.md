# SE-Sprint01-Team41

<h2>Contributors</h2>
<h3>Sprint 1<h3>

* Rajdeep Bastakoti

* Robert Xhafa

<h3>Sprint 2<h3>
 
* Mahdi Ouchrahou
 
* Aryans Rathi


<H2>About the project</H2>
<p>Corona Archive is a web service for Corona disease management which
enables digital tracking of citizens which enter certain places and keeping the records in case of a
Covid infection spread.</p>

<h3>Built with:</h3>

1. Flask
2. Python3
3. Html
4. Css
5. Mysql

## Using the App in your Machine
Follow these instructions to run the app in your device
### Prerequisites
Mysql
 
Flask
 
Sqlite3
 
Virtual Env
 
## File Structure

\--CoronaArchive
        
        \--static
            \--css                  # All the CSS Files used
        \--templates    
            \--                     # Main HTML files    
        \--sql  
            \--                     # SQL Query used for initialization
        \--tests
            |--test.py      # Main Testing Python Code
        -- app.py                    # Main Python Code
        -- README.md
        -- requirements.txt          # Required flask dependencies to run this program
     

 
### Installation Guide
#### Clone the repo. The following code:
#### git clone https://github.com/lorenzorota/se-02-team-15.git

#### Install virtual env
sudo pip3 install virtualenv

#### Create virtual environment
$ virtualenv env

#### Start virtual environment
$ source env/bin/activate

#### Install required dependencies like so:
$ pip install flask
 
$ pip install flask-mysqldb

#### Install Mysql DB for linux:
 
$ sudo apt-get install mysql-server
 
$ sudo apt-get install libmysqlclient-dev
 
$ pip3 install flask-mysqldb

#### Install qr code requirments:

$ pip install qrcode
 
###### Run this command in MYSQL command line to create required database.

 mysql> source sql/tables.sql

 mysql> exit

 ######  db.yaml file is already created

 ###### Open db.yaml and enter database credentials in the file format described below

 db.yaml
 
 ## [db.yaml] file Format. Enter your respective credentials

 We tried using ClamV so that it would be easier for the user. However clamv did not support the required flask dependices to run this program.
```mysql
mysql_host: "localhost"
mysql_user: "{YOUR USERNAME CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_password: "{YOUR PASSWORD CHANGE THIS WHEN TYPING IN YOUR COMPUTER}"
mysql_db: "seteam41"
```

#### Run python server for the app like so:
$ python3 app.py

#### Go to the app in your browser using following URL
http://http://127.0.0.1:5000/



<h1>Sprint 1 Progress</h1>

<h2>Frontend</h2>
1.	Created the main page where the user chooses his status and identity as a user. (whether he is a visitor, place owner, agent or hospital)<br>
2.	Created a login form for the visitor (email or phone number  and password to log in)<br>
3.	Created a registration form for the visitor (name, address, City, email and or phone, password etc..)<br>
4.	Created a login form for the place owner<br>
5.	Created a registration form for the place owner<br>

<h2>Backend</h2>
1.	Store the registered visitors and place owners in the data base<br>
2.	Login Authentication for the visitors and place owners that enter the right credentials  that match<br>

<h1>Sprint 2 Progress</h1>
 
 ✅ Created requirements.txt file, which was not provided.
 
 ✅ Changed the the database from sqlalchemy to Mysql.
 
 ✅ Fixed the frontend and made it more readable.
 
 ✅ Fixed registration process and connected it with the database.
 
 ✅ Created login system for Visitor, Owner, Agent, Hospitals.
 
 ✅ Created a QR generation system.
 
 ✅ Created a QR code scanner system.
 
 ✅ Created table.sql file for the database which was not provided.
 
 ✅ Added test for login and registration.
 
 ✅ Added test for each new page created. 
 
We were only given a simple frontend implementation from the first srpint. The backend was created using SQLAlchemy which was not suggested, now the backend is in Mysql per the schema. Almost 80% of the work has already been done now just some final backend code is left for other sprints. Now mulpitle Visitor, Owner and Hospitals can register and login using the correct credentials.
 
 Run this code once you are entire the environment

$ python3 test.py
 
 If there is any problem while running test and an error like no module named tkinter appears run the command

$ sudo apt-get install python3-tk

 There is also easy way to run this application. Just click on code download the zip file. Unzip it and run the app.py using python3 app.py command and install the requirnments as stated above.
