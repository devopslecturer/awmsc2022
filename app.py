from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/login-signup.html', methods = ['GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = ''
        #  User.query.filter_by(username=form.username.data).first()
        if check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('login'))
        return '<h1>Invalid username or password</h1>'
    return { "authenticated": True}
    # return render_template('login.html', form=form)


# @app.route('/login-signup.html', methods = ['POST'])
# def sign_up():
#     if request.method == 'POST':
#         FullName = request.form.get('su-name')
#         print(FullName)
#         Email = request.form.get('su-mail')
#         Password = request.form.get('su-pass')
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO cust_details VALUES(%s,%s,%s)''',(FullName,Email,Password))
#         mysql.connection.commit()
#         cursor.close()
#         return render_template('login-signup.html')
    
#     return render_template('login-signup.html')



if __name__ == '__main__': 
    app.run(host='localhost', port=5501)


# from flask import Flask, request, flash, url_for, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)


# class students(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200))
#     pin = db.Column(db.String(10))


# def __init__(self, name, city, addr, pin):
#     self.name = name
#     self.city = city
#     self.addr = addr
#     self.pin = pin


# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students=students.query.all())


# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash('Please enter all the fields', 'error')
#         else:
#             student = students(request.form['name'], request.form['city'],
#                                request.form['addr'], request.form['pin'])

#             db.session.add(student)
#             db.session.commit()
#             flash('Record was successfully added')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')


# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
