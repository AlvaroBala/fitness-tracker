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
    def get_all(cls, data):
        query = "SELECT * FROM calories LEFT JOIN users on calories.user_id=users.id where calories.user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        calories = []
        if results:
            for calorie in results:
                calories.append( calorie )
            return calories
        return calories
    # @staticmethod
    # def validate_calorie(calorie):
    #     is_valid = True
    #     # test whether a field matches the pattern
        
    #     if not len(calorie['num']):
    #         flash('Please set calories', 'num')
    #         is_valid = False

    #     return is_valid
    @classmethod
    def create_calorie(cls, data):
        query = "INSERT INTO calories (num, time,user_id) VALUES ( %(num)s,%(time)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)