from flask import Flask, render_template, request, redirect, session, g, url_for
from flask_mysqldb import MySQL
import yaml
import MySQLdb.cursors
import re
import os
import qrcode
from io import BytesIO

""" Login for the Agent page
Username=admin
Password=admin
After succesful login the page is redireacted to admin_page.html
"""


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='admin', password='admin'))

app = Flask(__name__)


""" Configure db"""

db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

""" sercet key for the admin page login"""
app.secret_key = os.urandom(16)


@app.route('/')
def index():
    return render_template('index.html')

"""__________ Registration Code__________________"""

@app.route('/register_visitor', methods=['GET', 'POST'])
def register_visitor():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        Visitor_name = userDetails['Visitor_name']
        user_name = userDetails['user_name']
        password = userDetails['password']
        email_id = userDetails['email_id']
        phone_number = userDetails['phone_number']
        city = userDetails['city']
        address = userDetails['address']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO VISITOR(Visitor_name, user_name,password,email_id, phone_number, city, address) VALUES(%s,%s,%s, %s, %s,%s,%s)", (Visitor_name, user_name, password, email_id, phone_number, city, address))
        mysql.connection.commit()
        cur.close()
        return render_template('login_visitor.html')
    return render_template('register_visitor.html')


@app.route('/register_place', methods=['GET', 'POST'])
def register_place():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        Place_name = userDetails['Place_name']
        user_name = userDetails['user_name']
        password = userDetails['password']
        email_id = userDetails['email_id']
        phone_number = userDetails['phone_number']
        city = userDetails['city']
        address = userDetails['address']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO PLACE(Place_name, user_name,password,email_id, phone_number, city, address) VALUES(%s,%s,%s, %s, %s,%s,%s)", (Place_name, user_name, password, email_id, phone_number, city, address))
        mysql.connection.commit()
        cur.close()
        return render_template('login_place.html')
    return render_template('register_place.html')


@app.route('/register_hospital', methods=['GET', 'POST'])
def register_hospital():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        Hospital_name = userDetails['Hospital_name']
        user_name = userDetails['user_name']
        password = userDetails['password']
        email_id = userDetails['email_id']
        phone_number = userDetails['phone_number']
        city = userDetails['city']
        address = userDetails['address']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO HOSPITAL(Hospital_name, user_name,password,email_id, phone_number, city, address) VALUES(%s,%s,%s, %s, %s,%s,%s)", (Hospital_name, user_name, password, email_id, phone_number, city, address))
        mysql.connection.commit()
        cur.close()
        return render_template('index.html')
    return render_template('register_hospital.html')


"""__________________ Login Codes__________________"""


@app.route('/login_hospital', methods=['GET', 'POST'])
def login_hospital():
   # Output message if something goes wrong...
    msg = 'Something went wrong'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Create variables for easy access
        user_name = request.form['user_name']
        password = request.form['password']
        # Check if account exists using MySQLs
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM HOSPITAL WHERE user_name = %s AND password = %s', (user_name, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # session['id'] = account['id']
            session['user_name'] = account['user_name']
            # Redirect to home page
            return render_template('index.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('login_hospital.html', msg=msg)


@app.route('/login_place', methods=['GET', 'POST'])
def place_log():
    # Output message if something goes wrong...
    msg = 'Something Went wrong'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Create variables for easy access
        user_name = request.form['user_name']
        password = request.form['password']
        # Check if account exists using MySQLs
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM PLACE WHERE user_name = %s AND password = %s', (user_name, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # session['id'] = account['id']
            session['user_name'] = account['user_name']
            # Redirect to home page
            return render_template('in_place.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('login_place.html', msg=msg)


@app.route('/login_visitor', methods=['GET', 'POST'])
def visitor_log():
    # Output message if something goes wrong...
    msg = 'Something Went Wrong'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Create variables for easy access
        user_name = request.form['user_name']
        password = request.form['password']
        # Check if account exists using MySQLs
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM VISITOR WHERE user_name = %s AND password = %s', (user_name, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # session['id'] = account['id']
            session['user_name'] = account['user_name']
            # Redirect to home page
            return render_template('in_visitor.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('login_visitor.html', msg=msg)


@app.route('/login_agent', methods=['GET', 'POST'])
def login_agent():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect("/agent_page")

        return redirect(url_for('/login_agent'))

    return render_template('login_agent.html')


@app.route('/agent_page')
def agent_page():
    return render_template('agent_page.html')


if __name__ == "__main__":
    app.run(debug=True)
