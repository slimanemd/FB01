#======================================================================================
#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#======================================================================================
app = Flask(__name__)                                              #app
app.config['SECRET_KEY'] = '441111cbb2e2bc8e2e1f274d185cc45e'      #config security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/site.db'        #db
db =  SQLAlchemy(app)                                              #Databasse
bcrypt = Bcrypt(app)


from flaskblog import routes