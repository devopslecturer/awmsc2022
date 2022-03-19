from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'wedwckd'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login_signup')
def load_login_page():
    return render_template('login_signup.html')

@app.route('/login_signup_check', methods = ['GET','POST'])
def login_signup():
    if request.method == 'GET':
        # print(request.args)
        email = request.args.get('email')
        password = request.args.get('password')
        cursor = mysql.connection.cursor()
        print('email',email, 'password', password)
        cursor.execute('''select * from cust_details where email=%s and Password=%s''',(email,password))
        result = cursor.fetchone()
        # print('result',result)
        if None != result and email == result[2] and password == result[3]:
            mysql.connection.commit()
            cursor.close()
            return render_template('profile.html')
        else: 
            mysql.connection.commit()
            cursor.close()
            return '<h1>not matched</h1>'

    if request.method == 'POST':
        firstname = request.args.get('su-name')
        lastname=request.args.get('su-lastname')
        Email = request.args.get('su-mail')
        Password = request.args.get('su-pass')  
        # print(Email)
        # print(Password)
        # print(lastname)
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO cust_details VALUES(%s,%s,%s,%s)''',(firstname,lastname,Email,Password))
        mysql.connection.commit()
        cursor.close()
        return '</h1>signed up</h2>'    
        
if __name__ == '__main__':
    app.debug = True
    app.run()
