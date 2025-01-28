from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models import dojo

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.dojo = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;"
        result = connectToMySQL(DB).query_db(query)

        ninjas = []
        if result:
            for row in result :
                ninja = cls(row)
                dojo_data = {
                    'id' : row ['dojos.id'],
                    'name' : row ['dojos.name'],
                    'created_at' : row ['dojos.created_at'],
                    'updated_at' : row ['dojos.updated_at'],
                }
                ninja.dojo = dojo.Dojo(dojo_data)
                ninjas.append(ninja)
                return ninjas
        
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name , last_name , age , dojo_id) VALUES (%(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s); "
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def update(cls , data):
        query = "UPDATE ninjas SET first_name = %(first_name)s , last_name = %(last_name)s , age = %(age)s; "
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def delete (cls , data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query ,data)
        return result

    
    @classmethod
    def get_by_id(cls , data):
        query ="""
            SELECT * FROM ninjas
            JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s ;
            """
        result = connectToMySQL(DB).query_db(query, data)
        if not result :
            return None
        
        ninja = cls(result[0])
        dojo_data = {
            'id' : result[0]['dojos.id'],
            'first_name' : result[0]['first_name'],
            'last_name' : result[0]['last_name'],
            'age' : result[0]['age'],
            'created_at' : result[0]['dojos.created_at'],
            'updated_at' : result[0]['dojos.updated_at'],

        }
        ninja.dojo = dojo.Dojo(dojo_data)
        return ninja

    
    


