from flask_app.models.user import User 
from flask_app.models.post import Post
from flask import request, redirect , render_template , session , flash
from flask_app import app

@app.route('/')
def index():
    return render_template('sign.html')

@app.route('/login')
def login():
    return render_template('sign.html')

@app.route('/register' , methods=['post'])
def registerr():
    data = request.form
    if User.validate_register(data):
        User.register(data)
        return redirect('/login')
    return redirect('/')

@app.route('/login' , methods=['post'])
def loginn():
    
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(request.form)

        session['email'] = data['email']
        session['user_id'] = user.id
        return redirect('/wall')
    return redirect('/')

@app.route('/wall')
def wall():

    data = {
        'id': session['user_id']
    }
    
    return render_template("wall.html", user=User.get_by_id(data))
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

