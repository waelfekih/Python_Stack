from flask import request, redirect , render_template , session , flash
from flask_app import app
from flask_app.models.loginregister import Loginregister

@app.route('/')
def ind():
    return redirect('/register')

@app.route('/register')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register' , methods =['post'] )
def register():
    data = request.form
    if Loginregister.validate_register(data):
        Loginregister.register(data)
        return redirect('/login')
    return redirect('/')


@app.route('/login' , methods =['post'] )
def login_success():
    data = request.form
    if Loginregister.validate_login(data):
        session['email'] = data['email']
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/dashboard')
def check():
    if 'email' in session:

        return render_template('dashboard.html')
    
    flash("You need to Sign In")
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
    
    


