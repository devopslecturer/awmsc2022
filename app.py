from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)


# app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(signup_bp, url_prefix='/signup')
# app.register_blueprint(login_bp, url_prefix='/login')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
