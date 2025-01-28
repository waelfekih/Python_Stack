from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.cookies import Cookie

@app.route('/')
def indexx():
        return redirect("/cookies" )


@app.route('/cookies')
def index():
    cookie = Cookie.get_all()
    return render_template('cookies.html',cookie = cookie)

@app.route('/cookies/create_order')
def create_ord():
      return render_template('create.html')

@app.route('/cookies/create_order' , methods =['post'])
def create():
      if Cookie.validate_order(request.form):
        Cookie.create_order(request.form)
        return redirect ('/cookies')
      return redirect('/cookies/create_order')

@app.route('/cookies/edit/<int:id>')
def edit(id):
     data = {
          'id': id
     }
     return render_template('edit.html' , n = id)

@app.route('/cookies/edit/<int:id>')
def edit_ord(id):
    d =Cookie.get_by_id(id)
    if Cookie.validate_order(request.form):
        Cookie.edit_order(request.form)
        return redirect ('/cookies')
    return redirect('/cookies/edit/<int:id>')
     

            