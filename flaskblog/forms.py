#======================================================================================
#import
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

#======================================================================================
#Classes
#Form Login
class LoginFormWithoutRemberMe(FlaskForm):
  #constructor
  def __init__(self, infos = None):
    super().__init__()
    self.infos = infos    

  email            = StringField  ('Email'           , validators =[DataRequired(), Email()] )
  password         = PasswordField('Password'        , validators =[DataRequired()] )
  submit           = SubmitField  ('Login')

#======================================================================================
#Form Login
class LoginForm(LoginFormWithoutRemberMe):  #FlaskForm):
  remember         = BooleanField('Remember Me')

#======================================================================================
#Form Register
class RegistrationForm(LoginFormWithoutRemberMe): #FlaskForm):
  username         = StringField  ('Username'        , validators =[DataRequired(), Length(min=2,max=5)] )
  confirm_password = PasswordField('Confirm Password', validators =[DataRequired(), EqualTo('password')] )

  #
  def validate_username(self, field):
    if User.isUserExist('username',field.data):
      raise ValidationError('VM: User name is taken, plz choose another yyyy')    
    
  #
  def validate_email(self, field):
    if User.isUserExist('email',field.data):
      raise ValidationError('VM: User email is taken, plz choose another xxxxxxx')
  