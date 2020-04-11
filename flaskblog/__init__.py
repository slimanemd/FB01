#======================================================================================
#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#======================================================================================
app = Flask(__name__)                                              #app
app.config['SECRET_KEY'] = '441111cbb2e2bc8e2e1f274d185cc45e'      #config security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/site.db'        #db
db =  SQLAlchemy(app)                                              #Databasse
bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)
login_manager.login_view =  'login'
login_manager.login_message_category = 'info'

from flaskblog import routes