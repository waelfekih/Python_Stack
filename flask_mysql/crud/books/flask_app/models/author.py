from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models import book


class Author :
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books =  []

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('books').query_db(query)
        
        authors = []
        for u in results:
            authors.append(cls(u))
        return authors
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (name , created_at , updated_at) VALUES (%(name)s , NOW() ,NOW());"
        result = connectToMySQL('books').query_db(query,data)
        return result
    
    @classmethod
    def unfavorited_authors(cls , data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        authors = []
        results = connectToMySQL('books').query_db(query , data)
        for row in results:
            authors.append(cls(row))
            return authors