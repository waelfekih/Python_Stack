from flask_app.config.mysqlconnection import DB, connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)

        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def get_by_id(cls , data):
        query ="SELECT * FROM dojos WHERE id = %(id)s ;"
            
        result = connectToMySQL(DB).query_db(query, data)
        if result :
            return cls[result[0]]
        return None
        
        
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @classmethod
    def get_one_w_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print (results)
        dojo = cls(results[0])
        for row in results : 
            n  = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at'],
            }
        dojo.ninjas.append(ninja.Ninja(n))
        return dojo

    
        


