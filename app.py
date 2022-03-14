from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'wedwckd'

# app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(signup_bp, url_prefix='/signup')
# app.register_blueprint(login_bp, url_prefix='/login')


@app.route('/')
def index():
    return render_template('html/Home.html')

@app.route('/login_signup')
def load_login_page():
    return render_template('html/login_signup.html')

@app.route('/login_signup_check', methods = ['GET','POST'])
def login_signup():
    if request.method == 'GET':
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mysql.connection.cursor()
        result = cursor.execute('''select * from cust_details where email=%s and Password=%s''',(email, password))
        # cursor.execute(''' INSERT INTO cust_details VALUES(%s,%s,%s)''',(FullName,Email,Password))
        mysql.connection.commit()
        cursor.close()
        print(email)
        print(password)
        return '</h1>logged in</h2>'

    if request.method == 'POST':
        firstname = request.form.get('su-name')
        Email = request.form.get('su-mail')
        Password = request.form.get('su-pass')
        lastname=''
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO cust_details VALUES(%s,%s,%s,%s)''',(firstname,lastname,Email,Password))
        mysql.connection.commit()
        cursor.close()
        return '</h1>signed up</h2>'    
        
if __name__ == '__main__':
    app.debug = True
    app.run()
