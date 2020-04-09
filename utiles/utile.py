#======================================================================================
#import
from forms import RegistrationForm, LoginForm
from flask import render_template, flash,  redirect, url_for #, Flask, request

#======================================================================================
#Helpers
#register route
def reglog(isSignUp):
  action = 'Register' if isSignUp else 'Login'
  if isSignUp :
    rlgForm = RegistrationForm({'title':'Register', 'submit':'Sign up'})
  else:
    rlgForm = LoginForm({'title':'Login', 'submit':'Login'})    

  #
  if rlgForm.validate_on_submit():
    #validation model u = u & pw = pw
    if rlgForm.email.data == 'slim@gml.com' and rlgForm.password.data == '123':
      flash( action + ' ' +'have succeded', 'success')
      return redirect(url_for('login' if isSignUp else 'home'))
    else:
      message = 'check your credential'
      flash(message, 'danger')

  # return GET default method
  return render_template('login.html', data={'isSignUp':isSignUp}, form=rlgForm)
