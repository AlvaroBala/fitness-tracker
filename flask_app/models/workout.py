from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import flash
# create a regular expression object that we'll use later   
class Workout:
    db_name = 'db'
    def __init__( self , data ):
        self.id = data['id']
        self.wname = data['wname']
        self.description = data['description']
        self.time = data['time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database


    @classmethod
    def get_workout_by_id(cls, data):
        query = 'SELECT * FROM workouts WHERE id= %(workout_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM workout LEFT JOIN users on workouts.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        workouts = []
        # Iterate over the db results and create instances of friends with cls.
        if results:
            for workout in results:
                workouts.append( workout )
            return workouts
        return workouts
    
    @classmethod
    def get_all_user_workout(cls, data):
        query = "SELECT * FROM workouts LEFT JOIN users on workouts.user_id = users.id WHERE workouts.user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        workouts = []
        if results:
            for workout in results:
                workouts.append( workout )
            # print(workouts)
            return workouts
        
        return workouts
    
    @classmethod
    def create_workout(cls, data):
        query = "INSERT INTO workouts (wname, description,time, user_id) VALUES ( %(wname)s, %(description)s,%(time)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    # @classmethod
    # def update_post(cls, data):
    #     query = "UPDATE posts SET title = %(title)s, content = %(content)s WHERE id = %(post_id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)
    
    # @classmethod
    # def delete_post(cls, data):
    #     query = "DELETE FROM posts WHERE id = %(post_id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)
    
    # @classmethod
    # def delete_all_user_posts(cls, data):
    #     query = "DELETE FROM posts WHERE user_id = %(user_id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)
    

    @staticmethod
    def validate_workout(workout):
        is_valid = True
        # test whether a field matches the pattern
        
        if len(workout['wname'])< 2:
            flash('Title must be more than 2 characters', 'wname')
            is_valid = False
        if len(workout['description'])< 2:
            flash('Post content must be more than 2 characters', 'description')
            is_valid = False
        # if not len(workout['time']):
        #     flash('please fill', 'time')
        #     is_valid = False
        
        return is_valid

    @classmethod
    def GetUserWhoFavouriteWorkouts(cls, data):
        query = "SELECT favourites.user_id as id from favourites where workouts_id =  %(workouts_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        workouts = []
        if results:
            for workout in results:
                workouts.append( workout ["id"])
            return workouts  
        return workouts
    
    @classmethod
    def addfavourite(cls, data):
        query = "INSERT INTO favourites (user_id, workout_id) VALUES ( %(user_id)s,%(workout_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def allfavourite(cls, data):
        query = "select * from favourites left join workouts on favourites.workout_id = workout_id where favourites.user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        favourites = []
        if results:
            for favourite in results:
                favourites.append( favourite )
            # print(workouts)
            return favourites
        
        return favourites