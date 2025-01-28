from flask_app import app
from flask import redirect , request ,render_template
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def home():
    return redirect ('/authors')

@app.route('/authors')
def dojos():
    users = Author.get_all()
    return render_template('authors.html',all_users = users)


@app.route('/authors/create', methods=['post'])
def create_user():
    Author.save(request.form)
    return redirect('/authors')