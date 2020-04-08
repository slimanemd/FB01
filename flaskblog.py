from data.dt_posts import *
from flask import Flask, render_template
app = Flask(__name__)

#home route
@app.route('/')
@app.route('/home')
def home():  #, 
  return render_template('home.html', data = {'user':user, 'posts': posts}) #'<h1>Hello World</h1>'

#about route
@app.route('/about')
def about():
  return render_template('about.html',data= {'title':title}) #'<h1>About Page</h1>'  

if __name__ == "__main__":
    app.run(debug=True)