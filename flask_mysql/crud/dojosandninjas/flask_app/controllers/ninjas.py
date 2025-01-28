from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import ninja , dojo



@app.route('/ninjas')
def ninjas(): 
    
    return render_template("ninjas.html"  , dojos = dojo.Dojo.get_all())



@app.route('/ninjas/create' , methods=['POST'])
def create_ninja():
    
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas/<int:id>/edit')
def edit_ninja(id):

    ninja_to_edit = ninja.Ninja.get_by_id({'id':id})
    return render_template('edit_ninja.html' , ninja = ninja_to_edit)