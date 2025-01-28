from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import DB , connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Registration
    @classmethod
    def register(cls , data):
        """
            data = {
                'first_name' : value ,
                'last_name' : value ,
                'email' : value , 
                'password' : value,            
            }
        """

        encrypted_password = bcrypt.generate_password_hash(data['password'])

        data = dict(data)

        data['password'] = encrypted_password

        query = "INSERT INTO users (first_name , last_name , email , password) VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s) ;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s ;"
        result = connectToMySQL(DB).query_db(query , data)

        if result ==() :
            return None
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM users WHERE id = %(id)s ;"
        result = connectToMySQL(DB).query_db(query , data)
        return cls(result[0])

    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)

        if not user_in_db:
            is_valid = False
            flash("You need to Sign Up" , "login")

        elif not bcrypt.check_password_hash(user_in_db.password , data['password']) :
            is_valid = False
            flash("Wrong Password" , "login")
        return is_valid
    
    @staticmethod
    def validate_register(data):
        """
            data = {
                'first_name' : value ,
                'last_name' : value ,
                'email' : value , 
                'password' : value,    
                'confirm_password' : value ,        
            }
        """
        is_valid = True
        user_in_db = User.get_by_email(data)

        if not EMAIL_REGEX.match(data['email']) :
            is_valid = False
            flash("Email format incorrect")

        if len(data['first_name']) < 2 :
            is_valid = False
            flash("First Name must be at least 2 characters length")

        if len(data['last_name']) < 2 :
            is_valid = False
            flash("Last Name must be at least 2 characters length")

        if data['confirm_password'] != data['password'] :
            is_valid = False
            flash("passwords must match")
        
        return is_valid


    

    