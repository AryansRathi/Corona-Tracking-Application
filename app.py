from flask import Flask, render_template, request, redirect, session, g, url_for
from flask_mysqldb import MySQL
import yaml
import MySQLdb.cursors
import re
import os
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

# Reload templates, so that during development changing the HTML files
# Doesn't require restarting the server
app.config['TEMPLATES_AUTO_RELOAD'] = True

mysql = MySQL(app)

""" sercet key for the admin page login"""
app.secret_key = os.urandom(16)


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
            "INSERT INTO VISITOR(Visitor_name, user_name,password,email_id, phone_number, city, address, infected) VALUES(%s,%s,%s, %s, %s,%s,%s, false)", (Visitor_name, user_name, password, email_id, phone_number, city, address))
        mysql.connection.commit()
        cur.close()
        return redirect('/login_visitor', code=302)
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
        return redirect('/login_place')
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
        return redirect('/login_hospital')
    return render_template('register_hospital.html')


"""__________________ Login Codes__________________"""


@app.route('/login_hospital', methods=['GET', 'POST'])
def login_hospital():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Output message if something goes wrong...
        msg = 'Something Went wrong'
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
            session['H_id'] = account['H_id']
            session['loggedin'] = True
            session['user_name'] = account['user_name']
            return redirect('/in_hospital')

        msg = 'Incorrect username/password!'
        # Show the login form with message (if any)
        return render_template('login_hospital.html', msg=msg)

    return render_template('login_hospital.html')


@app.route('/login_place', methods=['GET', 'POST'])
def place_log():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Output message if something goes wrong...
        msg = 'Something Went wrong'
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
            session['P_id'] = account['P_id']
            session['loggedin'] = True
            session['user_name'] = account['user_name']
            return redirect('/qrcode')

        msg = 'Incorrect username/password!'
        # Show the login form with message (if any)
        return render_template('login_place.html', msg=msg)

    return render_template('login_place.html')


@app.route('/login_visitor', methods=['GET', 'POST'])
def visitor_log():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'user_name' in request.form and 'password' in request.form:
        # Output message if something goes wrong...
        msg = 'Something Went Wrong'
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
            session['V_id'] = account['V_id']
            session['loggedin'] = True
            session['user_name'] = account['user_name']
            # Redirect to the scan page
            return redirect('/scan', code=302)

        # Account doesnt exist or username/password incorrect
        msg = 'Incorrect username/password!'
        return render_template('login_visitor.html', msg=msg)

    return render_template('login_visitor.html')


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

# The scan page. Only accessible to visitors after logging in


@app.route('/scan', methods=['GET'])
def render_scan_page():
    # Make sure the user is logged in
    if session.get('loggedin') != True:
        return render_template('login_visitor.html', msg='You are not logged in!')

    # Make sure the user is a visitor
    if session.get('V_id') == None:
        return render_template('login_visitor.html', msg='You are not logged in!')

    return render_template('in_visitor.html')

# Qr code page. Only accessible to place owners


@app.route('/qrcode', methods=['GET'])
def render_qrcode_page():
    # Make sure the user is logged in
    if session.get('loggedin') != True:
        return render_template('login_place.html', msg='You are not logged in!')

    # Make sure the user is a visitor
    if session.get('P_id') == None:
        return render_template('login_place.html', msg='You are not logged in!')

    place_id = session.get('P_id')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM PLACE WHERE P_id=%s', (place_id,))
    place = cursor.fetchone()

    return render_template('in_place.html', place_id=place_id, place_name=place.get('Place_name'))


@app.route('/agent_page')
def agent_page():
    return render_template('agent_page.html')


@app.route('/in_hospital')
def hospital_page():
    # If not logged in as a hospital
    if session.get('H_id') == None or session.get('loggedin') != True:
        return redirect('/login_hospital', code=302)

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM VISITOR')
    users = cursor.fetchall()

    return render_template('in_hospital.html', users=users)

# Change the visitor status


@app.route('/change_visitor_status', methods=['POST'])
def change_visitor_status():
    # If not logged in as a hospital
    if session.get('H_id') == None or session.get('loggedin') != True:
        return redirect('/login_hospital', code=302)

    form = request.form
    visitor_id = int(form.get('visitor_id'))
    infected = '1' if form.get('infected') == 'true' else '0'

    cur = mysql.connection.cursor()
    cur.execute("UPDATE VISITOR SET infected=%s WHERE V_id='%s';", (
        infected,
        visitor_id
    ))
    mysql.connection.commit()

    return {
        'ok': True,
    }


@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    # Post Request
    if session.get('V_id') == None or session.get('loggedin') != True:
        if request.method == 'POST':
            return {
                'ok': False,
                'message': 'You must be logged in as a visitor to check in'
            }
        return redirect('/login_visitor', code=302)

    place_id = request.args.get('place')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM PLACE WHERE P_id=%s', (place_id,))
    place = cursor.fetchone()

    if place == None:
        msg = 'That place was not found!'
        if request.method == 'POST':
            return {
                'ok': False,
                'message': msg
            }
        return msg

    if request.method == 'GET':
        return render_template('checkin.html', place_id=place_id, place_name=place.get('Place_name'))

    form = request.form
    entry_date = form.get('entry_date')
    exit_date = form.get('exit_date')
    entry_time = form.get('entry_time')
    exit_time = form.get('exit_time')

    # Insert into db
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO VISITOR_TO_PLACE(
            entry_date,
            exit_date,
            entry_time,
            exit_time,
            V_id,
            P_id
        ) VALUES (%s, %s, %s, %s, %s, %s);
    """, (
        entry_date,
        exit_date,
        entry_time,
        exit_time,
        str(session.get('V_id')),
        str(place_id),
    ))
    mysql.connection.commit()
    cur.close()

    return {
        'ok': True,
    }

# End the session


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/', code=302)


@app.route('/check_in')
def check_in():
    return render_template('checkin.html')


@app.route('/')
def index():
    return render_template('index.html')
