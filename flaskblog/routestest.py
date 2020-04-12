#======================================================================================
#imports

from flaskblog import app
from flask import render_template, request

#from flaskblog.data.dt_posts import posts
from flaskblog.models import Post, User
from flaskblog.utiles.utile import get_posts_for
#======================================================================================
#Routes
#Feature 1205202102 send email and reset password

#home route
@app.route('/')
@app.route('/home')
def home():
  #1205201734
  return user_posts("")
  
  #1205201719
  #posts , user =  get_posts_for("")
  #return render_template('home.html', data = {'posts':posts, 'user':None,  'mode':'HOME'})

  #1205201619
  ##---------
  #posts = Post.query.all()
  #Test http://localhost:5000/ + http://localhost:5000/?page=k

  #Feature 001 : Pagination
  #current_page = request.args.get('page',1,type=int)
  #posts = Post.query.paginate(page = current_page,per_page=5)
  #return render_template('home.html', data = {'posts':posts, 'mode':'HOME'})

  #1205201519
  #posts = Post.query.all()
  #return render_template('home.html', data = {'user':user, 'posts': posts}, mode='HOME')
  ##current_page = request.args.get('page',1,type=int)
  #posts = Post.query.paginate(page = current_page,per_page=5)
  ##posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = current_page,per_page=5)
  ##return render_template('home.html', data = {'posts':posts, 'mode':'HOME'})  

  #Feature 002 : Order posts
  #current_page = request.args.get('page',1,type=int)
  #posts = Post.query.order_by(Post.date_posted.desc())\
  #                  .paginate(page = current_page,per_page=5)

''''''
#1205201719
#user route
@app.route('/user/<string:username>')
def user_posts(username):
  posts , user =  get_posts_for(username)
  return render_template('home.html', data = {'posts':posts, 'user':user, 'mode':'HOME'})  
  #return render_template('user_posts.html', data = {'posts':posts, 'user':user, 'mode':'HOME'})    
  
''''''

#about route
@app.route('/about')
def about(): return None

#Login route
@app.route('/login' , methods= ['GET', 'POST'])
def login(): return None

#register route
@app.route('/register', methods=['GET','POST'])
def register(): return None

#Login route
@app.route('/logout')  # , methods= ['GET', 'POST']
def logout(): return None

#Login route
@app.route('/account', methods= ['GET', 'POST'])
def account():  return None

#new post route
@app.route('/post/new', methods= ['GET', 'POST'])
def new_post(): return None

#new post route
@app.route('/post/<int:post_id>')
def post(post_id): return None
