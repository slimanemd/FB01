#======================================================================================
#imports
from flaskblog.utiles.utile import reglog, processAccount, getPostForm, get_posts_for
from flaskblog import app
from flask import render_template, redirect, url_for, request
from flaskblog.data.dt_posts import user, posts, title
from flask_login import current_user, logout_user, login_required

from flaskblog.data.dt_posts import i18s

from flaskblog.models import Post
#======================================================================================
#Routes

#1205201734: home route
@app.route('/')
@app.route('/home')
def home():
  return user_posts("")

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
                          data        = {'title' :'Account', 'entity':'A', 'submit':i18s['en']['account_submit']},
                          image_file  = result['image'], 
                          form        = result['form'])


#new post route
@app.route('/post/new', methods= ['GET', 'POST'])
@login_required
def new_post():
  postForm =  getPostForm()
  if postForm == None: return  redirect(url_for('home'))
  return render_template('create_post.html',
                          data = {'title' :'New Post', 'entity':'P', 'submit':i18s['en']['new_post_submit']},
                          form = postForm)

#new post route
@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
  current_post = Post.query.get_or_404(post_id)
  return render_template('post.html',data={'title': current_post.title}, mode='SHOW', post = current_post)

#1205201719: user route
@app.route('/user/<string:username>')
def user_posts(username):
  posts , user =  get_posts_for(username)
  return render_template('home.html', data = {'posts':posts, 'user':user, 'mode':'HOME'})  
