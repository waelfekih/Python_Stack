from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import DB , connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Loginregister :
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #self.confirm_password = data['confirm_password']
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM register_login ;"
        results = connectToMySQL(DB).query_db(query)
        
        registre = []
        for r in results:
            registre.append(cls[r])
        return registre
    #Registration
    @classmethod
    def register (cls , data):
        """
            data = {
                'first_name' : value
                'last_name' : value
                'email' : value
                'password' : value
            }
        """

        encrypted_password = bcrypt.generate_password_hash(data['password'])

        data = dict(data)
        data['password'] = encrypted_password

        query = "INSERT INTO register_login (first_name , last_name , email , password) VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result

    @classmethod
    def get_by_email (cls , data) : 
        query = "SELECT * FROM register_login WHERE email = %(email)s "
        result = connectToMySQL(DB).query_db(query, data)
    
        if result ==():
            return None
        return cls(result[0])
    

    @staticmethod
    def validate_register(data):

        user_in_db = Loginregister.get_by_email(data)
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Email Format Incorrect")

        if user_in_db :
            is_valid = False
            flash("Email already exists")

        if len(data['first_name']) < 2 :
            is_valid = False
            flash("First Name should be at least 2 caracters length")

        if len(data['first_name']) < 2 :
            is_valid = False
            flash("Last Name should be at least 2 caracters length")

        if len(data['password']) < 8 :
            is_valid = False
            flash("Password should be at least 8 caracters length ")

        if data['password'] != data['confirm_password'] :
            is_valid = False
            flash("Passwords doesn't match")

        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = Loginregister.get_by_email(data)

        if not user_in_db : 
            is_valid = False
            flash("User doesn't exist")

        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            is_valid = False
            flash("Wrong password")
        return is_valid


        


        






         
