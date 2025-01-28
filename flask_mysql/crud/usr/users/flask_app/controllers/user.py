from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.users import User

@app.route('/')
def indexx():
    return redirect('/users')

@app.route('/users')
def index():
    users = User.get_all()
    return render_template("read_all.html" , user= users )

@app.route('/users/<int:id>')
def azer(id):
    user = User.get_one(id)
    return render_template("read_all.html")

@app.route('/users/create' , methods=['post'])
def create_user():
    if User.validate_newuser(request.form):
        User.create(request.form)
        return redirect('/users')
    return redirect("/users/create")


    

    

