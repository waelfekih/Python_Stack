from flask_app import app
from flask import render_template , request 
from flask_app.models.users import User

@app.route('/users')
def index():
    users = User.get_all()
    return render_template("read_all" , user= users )

@app.route('/users/<int:id>')
def azer(id):
    user = User.get_one(id)
    return render_template("read_all.html")

@app.route('/users/create')
def create_user():
    new = User.create()
    
    return render_template('create.html' ,user = new)


    

    

