from flask_app import app

from flask_app.models.user import User
from flask_app.models.recipe import Recipe 
from flask import request, redirect , render_template , session , flash

@app.route('/recipes')
def recipe():
    if not 'userEmail' in session:
        return redirect('/')
    userEmail = session['userEmail']
    user = User.get_by_email({'email' : userEmail})
    recipes = Recipe.get_all()
    return render_template('recipes.html' , logged_user = user , recipes = recipes)

@app.route('/recipes/new')
def recipe_new():
    if not 'userEmail' in session:
        return redirect('/')
    
    users_id = User.get_by_email({'email' : session['userEmail']}).id
    return render_template('recipes_new.html' , users_id = users_id )

@app.route('/recipes/new' , methods=['POST'])
def create_recipe():
    if not 'userEmail' in session:
        return redirect('/')
    
    if Recipe.validate_recipe(request.form):
        Recipe.create(request.form)
        return redirect('/recipes')
    return redirect('/recipes/new')

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    recipetoedit = Recipe.get_by_id({'id': id})
    return render_template("edit_recipe.html" , recipe = recipetoedit)

@app.route('/recipes/update' , methods=['POST'])
def update_recipe():
    data = request.form
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    userEmail = session['userEmail']
    user = User.get_by_email({'email' : userEmail})

    recipe = Recipe.get_by_id({'id':id})
    return render_template('recipe_show.html' , logged_user = user , recipe = recipe)

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    Recipe.delete({'id' :id})
    return redirect('/recipes')
