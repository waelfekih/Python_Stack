from flask_app import app
from flask import render_template, redirect , request
from flask_app.models.dojo import Dojo 

@app.route('/')
def home():

    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html',all_dojos = dojos)

@app.route('/dojos/create' , methods=['POST'])
def create_dojo():

    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
         'id' : id
    }
   

    return render_template("show_dojos.html"  , dojo = Dojo.get_one_w_ninjas(data))
                           
