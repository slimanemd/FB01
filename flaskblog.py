#======================================================================================
#imports
from utiles.utile import reglog
from data.dt_posts import *
from flask import Flask, render_template  #, redirect, url_for, flash, request

#======================================================================================
app = Flask(__name__)                                              #app
app.config['SECRET_KEY'] = '441111cbb2e2bc8e2e1f274d185cc45e'      #config security


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

#======================================================================================
#main
if __name__ == "__main__":
  app.run(debug=True)
#======================================================================================


  """   
    logForm = LoginForm({'title':'Login', 'submit':'Login'})
    #if request.method ==  'POST':
    if logForm.validate_on_submit():
      #validation model u = u & pw = pw
      if logForm.email.data == 'slim@gml.com' and logForm.password.data == '123':
        flash('have logged', 'success')
        return redirect(url_for('home'))
      else:
        flash('check your credential', 'danger')

    # return GET default method
    return render_template('login.html', data={'isSignUp':False}, form=logForm) 

  regForm = RegistrationForm({'title':'Register', 'submit':'Sign up'})

  if regForm.validate_on_submit():
    #validation model u = u & pw = pw
    flash('user register with {form.email.data}', 'success')
    return redirect(url_for('login'))

  # return GET default method
  return render_template('login.html', data={'isSignUp':True}, form=regForm)
  """
