from flask_app.config.mysqlconnection import DB , connectToMySQL


class User:

    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    
    # ! CRUD

    @classmethod
    def get_all(cls):
        query = " SELECT * FROM users;"
        results = connectToMySQL(cls,DB).query_db(query)
        users = []
        for row in results:
            
            users.append(cls(row))
        return users
    
    @classmethod
    def get_one(cls, id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': id}
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

        """
        result = 
        (
            {
                'id' : 1,
                'first_name' : "john",
                'last_name' : "Doe" , 
                'email' : "johndoe@gmail.com" ,
                'created_at' : " 17-12-2024 " ,
                'updated_at' : " 17-12-2024"
            }
            ,
            {
                'id' : 2,
                'first_name' : "jane",
                'last_name' : "Doe" , 
                'email' : "janedoe@yahoo.com" ,
                'created_at' : " 17-12-2024 " ,
                'updated_at' : " 17-12-2024"

            }
        )
        """

        
    
    @classmethod
    def create(cls , data):
        query="INSERT INTO users (first_name , last_name , email) VALUES (%(first_name)s , %(last_name)s , %(email)s);"
        result = connectToMySQL(cls, DB).query_db(query , data)
        users = []
        for user in result : 
            users.append(cls(user))
        
        return users
    
    @classmethod
    def update(cls , data): 
        query="UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query , data)
        
    
    @classmethod
    def destroy(cls , data): 
        query="DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query , data)
        
    
