from flaskblog.utiles.utile import reglog
from flaskblog.data.dt_posts import *

from flaskblog import app
from flask import render_template  #Flask, render_template  #, redirect, url_for, flash, request
from flaskblog.models import User, Post

#======================================================================================
#Routes

#home route
@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', data = {'user':user, 'posts': posts})

#about route
@app.route('/about')
def about():
  return render_template('about.html',data= {'title':title})

#Login route
@app.route('/login' , methods= ['GET', 'POST'])
def login():
  return reglog(False)

#register route
@app.route('/register', methods=['GET','POST'])
def register():
  return reglog(True)
