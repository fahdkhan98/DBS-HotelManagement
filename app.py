from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from datetime import datetime
import random
import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'hotel'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hotel'

mysql = MySQL(app)

@app.route('/', methods =['GET', 'POST'])
def index():
    msg=''
    if request.method=='POST' and 'email' in request.form and 'pass' in request.form:
        email = request.form['email']
        passw = request.form['pass']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE email = %s AND password = %s", (email, passw))
        data = cur.fetchone()
        if data:
            session['email'] = email
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            msg = 'Invalid username/password'
    return render_template('index.html', msg=msg)

@app.route('/dashboard', methods =['GET', 'POST'])
def dashboard():
    if session.get('loggedin'):
        return render_template('dashboard.html')

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/check', methods =['GET', 'POST'])
def check():
    if request.method == 'POST' and 'guest_id' in request.form:
        guest_id = request.form['guest_id']
        print(guest_id)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM book WHERE id = %s",(guest_id,))
        guest_data = cursor.fetchone()
        display_mode = 1
        return render_template('checkinfo.html', guest_data = guest_data, display_mode = display_mode)
    return render_template('checkinfo.html')

@app.route('/booking', methods =['GET', 'POST'])
def booking():
    msg=''
    if session.get('loggedin'):
        if request.method == 'POST' and 'name' in request.form and 'mobile' in request.form and 'checkin' in request.form and 'checkout' in request.form and 'number_of_rooms' in request.form and 'room_type' in request.form and 'price' in request.form and 'mode' in request.form:
            name = request.form['name']
            mobile = request.form['mobile']
            checkin = request.form['checkin']
            checkout = request.form['checkout']
            number_of_rooms = request.form['number_of_rooms']
            room_type = request.form['room_type']
            price = request.form['price']
            mode = request.form['mode']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO book VALUES (NULL,%s, %s, %s, %s, %s, %s, %s, %s)', (name, mobile, checkin, checkout, number_of_rooms, room_type, price, mode))
            mysql.connection.commit()
            msg = 'Booking Successful'
            return render_template('dashboard.html', msg=msg)
        return render_template('booking.html')
    return redirect(url_for('index'))

@app.route('/editbook', methods =['GET', 'POST'])
def editbook():
    if session.get('loggedin'):
        if request.args.get('guest_id'):
            guest_id = request.args.get('guest_id')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM book WHERE id = %s",(guest_id,))
            guest_data = cursor.fetchone()
            return render_template('editbooking.html', guest_data = guest_data)
        if request.method == 'POST' and 'name' in request.form and 'mobile' in request.form and 'checkin' in request.form and 'checkout' in request.form and 'number_of_rooms' in request.form and 'room_type' in request.form and 'price' in request.form and 'mode' in request.form and 'guest_id' in request.form:
            name = request.form['name']
            mobile = request.form['mobile']
            checkin = request.form['checkin']
            checkout = request.form['checkout']
            number_of_rooms = request.form['number_of_rooms']
            room_type = request.form['room_type']
            price = request.form['price']
            mode = request.form['mode']
            guest_id = request.form['guest_id']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE book SET name = %s, mobile = %s, check_in = %s, check_out = %s, number_of_rooms = %s, room_type = %s, price = %s, mode = %s WHERE id = %s",(name,mobile,checkin,checkout,number_of_rooms,room_type,price,mode,guest_id))
            mysql.connection.commit()
            msg = "Guest data has been updated successfully."
            return redirect(url_for('guestlist',msg=msg))

@app.route('/deletebook', methods =['GET', 'POST'])
def deletebook():
    if session.get('loggedin'):
        if request.args.get('guest_id'):
            guest_id = request.args.get('guest_id')
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("DELETE FROM book WHERE id = %s",(guest_id,))
            mysql.connection.commit()
            msg = "Guest data has been deleted successfully."
            return redirect(url_for('guestlist',msg=msg))

@app.route('/guestlist')
def guestlist():
    if session.get('loggedin'):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM book')
        guestdata = cursor.fetchall()
        if request.args.get('msg'):
            msg = request.args.get('msg')
            return render_template('guestlist.html', guestdata=guestdata, msg=msg)
        return render_template('guestlist.html', guestdata=guestdata)
    return redirect(url_for('index'))

@app.route('/roomsinfo')
def roomsinfo():
    return render_template('roomsinfo.html')

@app.route('/roomservice')
def roomservice():
    if session.get('loggedin'):
        return render_template('roomservice.html')
    return redirect(url_for('index'))

@app.route('/verifyguestid', methods =['GET', 'POST'])
def verifyguestid():
    if request.method == 'POST' and 'guestid' in request.form:
        guestid = request.form['guestid']   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM book WHERE id = %s', (guestid,))
        guestdata = cursor.fetchone()
        if guestdata is None:
            return 1
        else:
            return guestdata                                                           

def getroomtype(roomtype):
    if roomtype == '1':
        return 'Hollywood Twin Room'
    elif roomtype == '2':
        return 'Studio'
    elif roomtype == '3':
        return 'Mini Suite'
    elif roomtype == '4':
        return 'Villa'
app.jinja_env.globals.update(getroomtype=getroomtype) 

def get_guest_check_badge(guest_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM book WHERE id = %s",(guest_id,))
    guest_data = cursor.fetchone()
    check_out = guest_data['check_out']
    current_time = datetime.now()
    current_time = current_time.strftime("%Y-%m-%d")
    current_time = datetime.strptime(current_time, "%Y-%m-%d")
    current_time = current_time.date()
    if check_out > current_time:
        return 1
    else:
        return 2
app.jinja_env.globals.update(get_guest_check_badge=get_guest_check_badge) 

def get_book_mode_selected(guest_md,md):
    md = str(md)
    if guest_md == md:
        return 'selected'
app.jinja_env.globals.update(get_book_mode_selected=get_book_mode_selected) 

def get_book_room_type_selected(guest_room_type,room_type):
    room_type = str(room_type)
    if guest_room_type == room_type:
        return 'selected'
app.jinja_env.globals.update(get_book_room_type_selected=get_book_room_type_selected) 