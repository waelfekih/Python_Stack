from flask_app import app
from flask import render_template , redirect , request
from flask_app.models.author import Author 
from flask_app.models.book import Book



@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html',all_books = books)

@app.route('/books/create', methods=['post'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/join/author' , methods = ['post'])
def join_author():
    data = {
        'author_id':request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect (f"/book/{request.form['book_id']}")
