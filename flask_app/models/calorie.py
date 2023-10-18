from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash
# create a regular expression object that we'll use later   
class Calorie:
    db_name = 'db'
    def __init__( self , data ):
        self.id = data['id']
        self.num = data['num']
        self.time = data['time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_calorie_by_id(cls, data):
        query = 'SELECT * FROM calories WHERE id= %(calorie_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM calorie LEFT JOIN users on calories.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        calories = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for calorie in results:
                calories.append( calorie )
            return calories
        return calories