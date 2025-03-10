from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models import author

class Book :
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        #self.updated_at = data['updated_at']

        self.authors_who_favorited = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books').query_db(query)
        
        books = []
        for b in results:
            books.append(cls(b))
        return books
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title , num_of_pages) VALUES (%(title)s , %(num_of_pages)s);"
        result = connectToMySQL('books').query_db(query,data)
        return result
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query , data)

        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break

            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at" : row['authors.updated_at']

            }
            book.authors_who_favorited.append(author.Author(data))
            return book