from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
# from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv, path
from dotenv import load_dotenv

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'sql4.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql4480309'
app.config['MYSQL_PASSWORD'] = 'ywtgHyDEsc'
app.config['MYSQL_DB'] = 'sql4480309'
# app.config['MYSQL_PORT'] = 3306

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

    if request.method == 'POST':
        fullname = request.form.get('su-name')
        email = request.form.get('su-mail')
        password = request.form.get('su-pass')  
        # print(Email)
        # print(Password)
        # print(lastname)
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO customer_details (fullname, email, password) VALUES (%s,%s,%s)''',(fullname, email, password))
        mysql.connection.commit()
        cursor.close()
        return '</h1>signed up</h2>'    
        
if __name__ == '__main__':
    app.debug = True
    app.run()
    # basedir = path.abspath(path.dirname(__file__))
    # load_dotenv(path.join(basedir[:basedir.rindex('\\')], "dev.env"))  # Load environment variables from dev.env
    # remote_host_address = getenv("REMOTE_HOST")  # get remote host environment variable