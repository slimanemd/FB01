#======================================================================================
#imports
from flaskblog.utiles.utile import reglog, processAccount
from flaskblog import app
from flask import render_template, redirect, url_for, request
from flaskblog.data.dt_posts import user, posts, title
from flask_login import current_user, logout_user, login_required

from flaskblog.data.dt_posts import i18s
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
  return render_template('about.html',data= {'title':i18s['en']['about_title']})

#Login route
@app.route('/login' , methods= ['GET', 'POST'])
def login():
  if current_user.is_authenticated: return redirect(url_for('home'))

  #
  reglogFrm = reglog(False)
  if reglogFrm == None:  
    next_page =  request.args.get('next')
    return  redirect(next_page) if next_page else redirect(url_for('home'))
  return render_template('login.html', 
                          data = {'title' :'Login', 'isSignUp':False, 'entity':'L', 
                                  'submit':i18s['en']['login_submit']}, 
                          form = reglogFrm)  

#register route
@app.route('/register', methods=['GET','POST'])
def register():
  if current_user.is_authenticated: return redirect(url_for('home'))

  #
  reglogFrm = reglog(True)
  if reglogFrm == None: return redirect(url_for('login'))
  return render_template('login.html', 
                          data={'title' :'Register', 'isSignUp':True, 'entity':'R',
                                'submit':i18s['en']['register_submit']}, 
                          form=reglogFrm)

#Login route
@app.route('/logout')  # , methods= ['GET', 'POST']
def logout():
  logout_user()
  return redirect(url_for('home'))

#Login route
@app.route('/account', methods= ['GET', 'POST'])
@login_required
def account():
  #return render_template('account.html', data = {'user':'user', 'message': 'Hello to Account'})
  result = processAccount()  #account_image_file, account_form
  if result == None: return redirect(url_for('account'))
  return render_template('login.html', 
                          data        = {'title' :'Account', 'entity':'A',
                                         'submit':i18s['en']['account_submit']},
                          image_file  = result['image'], 
                          form        = result['form'])


