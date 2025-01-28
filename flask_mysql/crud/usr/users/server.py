from flask import Flask , render_template , redirect , request
from flask_app.models.users import User
app =Flask( __name__)
app.secret_key= "wael"
@app.route('/')
def showuser():
    
    return redirect('/users')
    
@app.route('/users')
def userlist():

    return render_template("read_all.html")

@app.route('/users/create')
def new_user():
    return render_template('create.html')

@app.route('/users/create' , methods=['post'])
def create_user():
    if User.validate_newuser(request.form):
        User.create(request.form)
        return redirect('/users')
    return redirect("/users/create")

@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html' , user=User.get_one(data))

@app.route('/users/show/<int:id>')
def show():
    data = {
        "id":id
    }
    return render_template("show_user.html" , user = User.get_one(data))


@app.route('/users/update' , methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)