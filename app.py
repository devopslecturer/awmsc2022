from flask import Flask, render_template, request
from flask_mysqldb import MySQL

"""
app.py code is shown here. This is a functionality to test the sphinx for auto documentation.
"""

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'sql4.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql4483888'
app.config['MYSQL_PASSWORD'] = 'qVFgSDccKM'
app.config['MYSQL_DB'] = 'sql4483888'
app.config['MYSQL_PORT'] = 3306

# route to home page when / is present in url
@app.route('/')
def index():

    """

    Description : The "index" function is used to handle the \/\ character in the URL while calling from app.py

    Return File : home.html
    
    Return Type : HTML

    """

    return render_template('home.html')

# route to home page when url points to "/home"
@app.route('/home.html')
def load_home_page():

    """

    Description : The "load_home_page" function is used to call the Homepage from python app.py

    Return File : home.html
    
    Return Type : HTML

    """

    return render_template('home.html')

# route to login_signup page when url points to "/home"
@app.route('/login_signup')
def load_login_page():

    """

    Description : The "load_login_page" function is used to call the Register and Login page from python app.py

    Return File : login_signup.html
    
    Return Type : HTML

    """

    return render_template('login_signup.html')

# route to check whether login or signup to render depending on method call
@app.route('/login_signup_check', methods = ['GET','POST'])
def login_signup():
    
    """

    Description : The section of the "login_signup" function is used to login the customer details into the database using login_signup.html from python app.py

    Return File : profile.html
    
    Return Type : HTML

    """
  
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        cursor = mysql.connection.cursor()
        print('email',email, 'password', password)
        cursor.execute('''select * from customer_details where email=%s and password=%s''',(email,password))
        result = cursor.fetchone()
        print('result',result)
        if None != result and email == result[1] and password == result[2]:
            mysql.connection.commit()
            cursor.close()
            return render_template('profile.html')
        else: 
            mysql.connection.commit()
            cursor.close()
            return '<h1>not matched</h1>'
            
    """

    Description : The section of the "login_signup" function is used to register the customer details into the database using login_signup.html from python app.py

    Return File : login_signup.html
    
    Return Type : HTML

    """
    
    if request.method == 'POST':
        fullname = request.form.get('su-name')
        email = request.form.get('su-mail')
        password = request.form.get('su-pass')  
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO customer_details (fullname, email, password) VALUES (%s,%s,%s)''',(fullname, email, password))
        mysql.connection.commit()
        cursor.close()
        return render_template('login_signup.html', confirm_message='registration successful')   # pop up for registration

# route to bookings page 
@app.route('/bookings.html')
def load_bookings_page():

    """

    Description : The "load_bookings_page" function is used to call the Bookings/ Rides page from python app.py

    Return File : bookings.html
    
    Return Type : HTML

    """

    return render_template('bookings.html')

# route to profile page
@app.route('/profile.html')
def load_profile_page():

    """

    Description : The "load_profile_page" function is used to call the profiles page from python app.py

    Return File : profile.html
    
    Return Type : HTML

    """
 
    return render_template('profile.html')

# route to payment page
@app.route('/payment.html')
def load_payment_page():

    """

    Description : The "load_payment_page" function is used to call the payment page from python app.py

    Return File : payment.html
    
    Return Type : HTML

    """
 
    return render_template('payment.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
