

## Corona Tracking Application
 
	
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
#### git clone https://github.com/AryansRathi/Corona-Tracking-Application.git

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
