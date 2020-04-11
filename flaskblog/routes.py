#======================================================================================
#imports
from flaskblog.utiles.utile import reglog
from flaskblog import app
from flask import render_template, redirect, url_for, request
from flaskblog.data.dt_posts import user, posts, title
from flask_login import current_user, logout_user, login_required
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
  if current_user.is_authenticated: return redirect(url_for('home'))

  #
  reglogFrm = reglog(False)
  if reglogFrm == None:  
    next_page =  request.args.get('next')
    return  redirect(next_page) if next_page else redirect(url_for('home'))
  return render_template('login.html', data={'isSignUp':False}, form=reglogFrm)  

#register route
@app.route('/register', methods=['GET','POST'])
def register():
  if current_user.is_authenticated: return redirect(url_for('home'))

  #
  reglogFrm = reglog(True)
  if reglogFrm == None: return redirect(url_for('login'))
  return render_template('login.html', data={'isSignUp':True}, form=reglogFrm)

#Login route
@app.route('/logout')  # , methods= ['GET', 'POST']
def logout():
  logout_user()
  return redirect(url_for('home'))

#Login route
@app.route('/account')  # , methods= ['GET', 'POST']
@login_required
def account():
  return render_template('account.html', data = {'user':'user', 'message': 'Hello to Account'})