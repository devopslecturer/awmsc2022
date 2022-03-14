from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('/Wed_wicked_adv_code/html/Home.html')


@app.route('/Wed_wicked_adv_code/html/login-signup.html', methods=['GET'])
def login():

    return render_template('/Wed_wicked_adv_code/html/login-signup.html')


@app.route('/Wed_wicked_adv_code/html/login-signup.html', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        FullName = request.form.get('su-name')
        print(FullName)
        Email = request.form.get('su-mail')
        Password = request.form.get('su-pass')
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO cust_details VALUES(%s,%s,%s)''', (FullName, Email, Password))
        mysql.connection.commit()
        cursor.close()
        return render_template('/Wed_wicked_adv_code/html/login-signup.html')

    return render_template('/Wed_wicked_adv_code/html/login-signup.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5501)
