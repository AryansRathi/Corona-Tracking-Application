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


"""____QR Code___________"""


def generate_qr_code(data, id):
    # Initialize the qr code generator with configuration like version, shape and size
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add Data to the qr code
    qr.add_data(data)

    # Generate the qr code
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Return the qr code
    return img


"""_________Registration code_______________"""


"""Registration of the Visitor.
   After successfull registration the page is
   redireacted to itself.
"""


@app.route('/visitor_registration', methods=['GET', 'POST'])
def visitor_info():
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
        return render_template('visitor_log.html')
    return render_template('visitor_registration.html')


"""Owner registration code """


@app.route('/place_registration', methods=['GET', 'POST'])
def place_registration():
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

        # Data to fill the qr code
        qr_data = Place_name + " " + city + " " + address + " " + email_id

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Place(Place_name, user_name,password,email_id, phone_number, city, address, qr) VALUES(%s,%s,%s, %s, %s,%s,%s,%s)", (Place_name, user_name, password, email_id, phone_number, city, address, qr_data))
        mysql.connection.commit()
        cur.close()

        return render_template('qr.html', qr_code=qr_data)
    return render_template('place_registration.html')


"""Hospital registration code"""


@app.route('/hospital_registration', methods=['GET', 'POST'])
def hospitaö_registration():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        hospital_name = userDetails['hospital_name']
        user_name = userDetails['user_name']
        password = userDetails['password']
        email_id = userDetails['email_id']
        phone_number = userDetails['phone_number']
        city = userDetails['city']
        address = userDetails['address']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO HOSPITAL (hospital_name, user_name,password,email_id, phone_number, city, address) VALUES(%s,%s,%s, %s, %s,%s,%s)", (hospital_name, user_name, password, email_id, phone_number, city, address))
        mysql.connection.commit()
        cur.close()
        return render_template('agent_page.html')
    return render_template('hospital_registration.html')


"""____________________Login codes________________________"""


"""Agent login code"""


@app.route('/agent_log', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect("/agent_page")

        return redirect(url_for('/agent_log'))

    return render_template('agent_log.html')


""" Login for visitor code """


@app.route('/visitor_log', methods=['GET', 'POST'])
def visitor_log():
    # Output message if something goes wrong...
    msg = ''
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
            return render_template('scan_qr.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('visitor_log.html', msg=msg)


"""Login for place """


@app.route('/place_log', methods=['GET', 'POST'])
def place_log():
    # Output message if something goes wrong...
    msg = ''
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
            return render_template('example.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('place_log.html', msg=msg)


""" Hospital login code """


@app.route('/hospital_log', methods=['GET', 'POST'])
def hospital_log():
    # Output message if something goes wrong...
    msg = ''
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
            return render_template('hospital_page.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)

    return render_template('hospital_log.html', msg=msg)


"""_________QR CODE_________________"""


"""____________Routes________________"""


@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def home():
    return render_template('about.html')


@app.route('/visitor')
def visitor():
    return render_template('visitor.html')


@app.route('/visitor_registration')
def visitor_registration():
    return render_template('visitor_registration.html')


@app.route('/agent_log')
def agent_log():
    return render_template('agent_log.html')


@app.route('/place')
def place():
    return render_template('place.html')


@app.route('/agent_page')
def agent_page():
    return render_template('agent_page.html')


@app.route('/hospital_registration')
def hospital_registration():
    return render_template('hospital_registration.html')


@app.route('/scan_qr')
def scan_qr():
    return render_template('scan_qr.html')


@app.route('/hospital_page')
def hospital_page():
    return render_template('hospital_page.html')


@app.route('/qr')
def qr():
    return render_template('qr.html')


if __name__ == '__main__':
    app.run(debug=True)
