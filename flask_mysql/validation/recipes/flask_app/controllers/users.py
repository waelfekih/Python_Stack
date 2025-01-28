from flask_app.models.user import User 
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

        session['userEmail'] = data['email']
        return redirect('/recipes')
    return redirect('/')

#@app.route('/recipes')
#def recipe():
    #data = {
        #'id':session['user_id']
    #}
    #return render_template('recipes.html' , recipe = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')