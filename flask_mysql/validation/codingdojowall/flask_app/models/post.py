from flask_app.config.mysqlconnection import connectToMySQL ,DB
from flask import flash
from flask_app.models.user import User

class Post:
    def __init__(self , data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

    @classmethod
    def create_com(cls , data):
        query = "INSERT INTO posts (content , user_id) VALUES (%(content)s , %(user_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def delete(cls , post_id):
        query = "DELETE FROM posts WHERE id = %(id)s ;"
        result = connectToMySQL(DB).query_db(query , {'id': post_id})
        return result
    
    @classmethod
    def validate_post(cls , data):
        is_valid = True
        if len(data['content']) == 0 :
            flash("Post content can not be blank")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM posts
        JOIN users ON users.id = posts.user_id;"""
        results = connectToMySQL(DB).query_db(query)

        all_posts = []

        for row in results:
            posting_user = User({
                "id": row["user_id"],
                "email": row["email"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
                "password": row["password"]
            })
            new_post = Post({
                "id": row["id"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user": posting_user
            })
            all_posts.append(new_post)

        return all_posts


    

        