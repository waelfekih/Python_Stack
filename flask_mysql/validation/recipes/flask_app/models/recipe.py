from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask import flash , request
from flask_app.models.user import User

class Recipe:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def create(cls ,data):
        query = "INSERT INTO recipes (name , description , instructions ,date_made , under , users_id) VALUES (%(name)s , %(description)s , %(instructions)s , %(date_made)s , %(under)s , %(users_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def update(cls , data):
        query = "UPDATE recipes SET name = %(name)s , description = %(description)s, instructions = %(instructions)s , date_made = %(date_made)s ,under = %(under)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query  , data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        selection = request.form.get("under")

        if len(data["name"]) < 3:
            flash("Name content must not be blank." , "name")
            is_valid = False
        if len(data["description"]) < 3 :
            flash("Description content must not be blank." , "description")
            is_valid = False
        if len(data["instructions"]) < 3:
            flash("Instructions content must not be blank." , "instructions")
            is_valid = False
        if data['date_made'] == "":
            flash("Wrong Date Format" , "date_made")
            is_valid = False
        if not selection :
            flash('Select an Option' , "under")
            is_valid = False
        
        
        return is_valid
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        if not result:
            return None

        recipe = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['users.created_at'],
            'updated_at': result[0]['users.updated_at'],
        }
        recipe.user = User(user_data)
        return recipe


    @classmethod
    def get_all(cls):
        query ="SELECT * FROM recipes JOIN users ON recipes.users_id = users.id ;"
        result  = connectToMySQL(DB).query_db(query)

        recipes = []
        if result:
            for row in result:
                recipe = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                recipe.user = User(user_data)
                recipes.append(recipe)
        return recipes
    

    


        
            


                
    
    

