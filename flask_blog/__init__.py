from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '33e691769378c0ad911e5a951faccdf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=  Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category ='info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'xda2.aditya@gmail.com'
app.config['MAIL_PASSWORD'] = 'adi@1996'
mail = Mail(app)

from flask_blog import routes