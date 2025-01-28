from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask_app.controllers import cookie
from flask import flash


class Cookie :
    def __init__(self , data):
        self.id = data['id']
        self.costumer_name = data['costumer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies ; "
        results = connectToMySQL('cookies_schema').query_db(query)
        
        cookies = []
        for c in results:
            cookies.append(cls(c))
        return cookies
    
    @classmethod 
    def create_order(cls , data):
        query = "INSERT INTO cookies (costumer_name , cookie_type , num_of_boxes) VALUES (%(costumer_name)s , %(cookie_type)s  , %(num_of_boxes)s );" 
        result = connectToMySQL('cookies_schema').query_db(query , data)
        return result
    
    @classmethod
    def get_by_id(data):
        query = "SELECT * FROM cookies WHERE id = %(id)s ;"
        result = connectToMySQL('cookies_schema').query_db(query , data)
        return result
    
    @classmethod
    def edit_order(data):
        query = "UPDATE cookies SET costumer_name = %(costumer_name)s , cookie_type = %(cookie_type)s , num_of_boxes = %(num_of_boxes)s WHERE id = %(id)s ; "
        result = connectToMySQL('cookies_schema').query_db(query , data)
        return result
    
    @staticmethod
    def validate_order(data):
        """
        data = {
        'costumer_name' = value ,
        'cookie_type' = value ,
        'num_of_boxes' = value,
        }
        """

        is_valid = True

        if len(data['costumer_name']) < 1 :
            is_valid = False
            flash("You should enter a valid Name")

        if len(data['cookie_type']) < 1 :
            is_valid = False
            flash("You should enter a valid cookie type")

        if int(data['num_of_boxes']) < 1 :
            is_valid = False
            flash("The minimum number of boxes is 1")
        
        return is_valid
    
    

        