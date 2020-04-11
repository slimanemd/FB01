#======================================================================================
#import
from flask import flash

#App
from flaskblog.data.dt_posts import i18s
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User
from flaskblog import db, bcrypt
from flask_login import login_user, current_user
from flask import redirect, url_for

#======================================================================================
#Helpers

#Lambda expression hash & decode
fcHash = lambda msg : bcrypt.generate_password_hash(msg).decode('utf-8')

#
def validateAction(actionInfos):
  user = User.query.filter_by(email = actionInfos['email']).first()
  if user and bcrypt.check_password_hash(user.password, actionInfos['password']): return user
  return None

#register route   'Sign up'
def reglog(isSignUp):
  #
  action = 'register' if isSignUp else 'login'
  rlgForm = ( RegistrationForm({'title':action,  'submit':i18s['en'][action]}) if isSignUp else 
              LoginForm       ({'title': action, 'submit':i18s['en'][action]}))

  #validation
  if rlgForm.validate_on_submit():
    if action == 'register': 
      #model
      user = User(username = rlgForm.username.data, 
                    email    = rlgForm.email.data, 
                    password = fcHash(rlgForm.password.data))
      db.session.add(user)
      db.session.commit()

      #
      actionInfos = {'message': action + ' ' +'user created with success', 'status':'success'}
      rlgForm = None  #success
    else:
      #model validation model u = u & pw = pw
      user = validateAction({'email':rlgForm.email.data, 'password':rlgForm.password.data})      
      if user:
        login_user(user, remember= rlgForm.remember.data)

        #
        actionInfos = {'message': action + ' ' +'have succeded', 'status':'success'}
        rlgForm = None  #success
      else:
        actionInfos = {'message': 'check your credentials', 'status':'danger'}
    #
    flash(actionInfos['message'], actionInfos['status'])
  
  return rlgForm 
  
  