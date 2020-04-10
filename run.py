from flaskblog import app

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
