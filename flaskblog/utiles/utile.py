#======================================================================================
#import
import secrets
import os
from PIL import Image

#
from flask import flash

#App
from flaskblog.data.dt_posts import i18s
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user
from flask import redirect, url_for, request

#======================================================================================
#Helpers

#Lambda expression hash & decode
fcHash             = lambda msg  : bcrypt.generate_password_hash(msg).decode('utf-8')
build_picture_flnm = lambda flnm : secrets.token_hex(8) + os.path.splitext(flnm)[1]
build_picture_path = lambda flnm : os.path.join(app.root_path, 'static/img',flnm)

#
def save_picture(form_picture):
  picture_fn = build_picture_flnm(form_picture.filename)  # output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail((125, 125))  #output_size)       #i.save(build_picture_path()picture_path)
  i.save(build_picture_path(picture_fn))

  #
  return picture_fn

#
def validateAction(actionInfos):
  user = User.query.filter_by(email = actionInfos['email']).first()
  if user and bcrypt.check_password_hash(user.password, actionInfos['password']): return user
  return None

#register route   'Sign up'
def reglog(isSignUp):
  #
  action = 'register' if isSignUp else 'login'
  rlgForm = ( RegistrationForm({'title':action, 'submit':i18s['en'][action + '_submit']}) if isSignUp else 
              LoginForm       ({'title':action, 'submit':i18s['en'][action + '_submit']}))

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

# processAccount
def processAccountForm():
  #return render_template('account.html', data = {'user':'user', 'message': 'Hello to Account'})
  acform = UpdateAccountForm({'title':'Account', 'submit':i18s['en']['account_submit']})  #
  if acform.validate_on_submit():
    if acform.picture.data: current_user.image_file = save_picture(acform.picture.data) #**
    current_user.username = acform.username.data
    current_user.email    = acform.email.data
    db.session.commit()
      
    #
    flash('Your account has been updated!', 'success')
    return None #redirect(url_for('account'))
  elif request.method == 'GET':
    #
    acform.username.data = current_user.username
    acform.email.data    = current_user.email

  return acform

#
def processAccount():
  #
  account_form = processAccountForm()
  if account_form:
    account_image_file = url_for('static', filename='img/' + current_user.image_file)
    return {'image':account_image_file, 'form':account_form}
  else:
    return None
