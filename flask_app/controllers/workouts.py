from flask_app import app

from flask import render_template, redirect, session, request, flash,url_for

from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_app.models.calorie import Calorie


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/add/workout')
def addWorkout():
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    }
    return render_template('workoutHistory.html',loggedUser = User.get_user_by_id(loggedUserData))
@app.route("/add/workout", methods=['POST'])
def createWorkout():
    if 'user_id' not in session:
        return redirect('/')

    if not Workout.validate_workout(request.form):
        return redirect(request.referrer)

    data = {
        'wname': request.form['wname'],
        'description': request.form['description'],
        'time': request.form['time'],
        'user_id': session['user_id']
    }

    Workout.create_workout(data)

    for i in range(2, 6):
        wname_key = f'wname{i}'
        description_key = f'description{i}'

        if wname_key in request.form and request.form[wname_key] != '':
            data = {
                'wname': request.form[wname_key],
                'description': request.form[description_key],
                'time': request.form['time'],
                'user_id': session['user_id']
            }
            Workout.create_workout(data)

    return redirect('/')

# @app.route('/workoutHistory')
# def workoutHistory():
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'user_id': session['user_id'],
#         'workout_id': id
        
#     } 
#     loggedUser = User.get_user_by_id(data)
#     workout = Workout.get_workout_by_id(data)

#     if not loggedUser:
#         return redirect('/logout')
#     return render_template('workoutHistory.html', workouts = Workout.get_all(), loggedUser = User.get_user_by_id(data),workout = workout)

@app.route('/workoutHistory')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    }
    return render_template('workoutHistory.html',loggedUser = User.get_user_by_id(loggedUserData), workout = Workout.get_all_user_workout(loggedUserData))

# @app.route('/add/workout', methods=['POST'])
# def add_workout():
#     wname = request.form['wname']
#     description = request.form['description']
#     time = request.form['time']
#     user_id = 1  # Replace with the actual user ID or get it from your authentication system

#     # Check validation (you can use the validate_workout method here)

#     workout_data = {
#         'wname': wname,
#         'description': description,
#         'time': time,
#         'user_id': user_id
#     }

#     # Use the create_workout method to insert the data into the database
#     workout_id = Workout.create_workout(workout_data)

#     if workout_id:
#         flash('Workout created successfully', 'success')
#     else:
#         flash('Failed to create workout', 'error')

#     return redirect(url_for('workoutHistory'))
@app.route('/calculate/calorie')
def add_calorie(id):
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    }
    data={
        'user_id': session['user_id'],
        'num': request.form['num'],
        'time': request.form['time']  
    }
    Calorie.addfavourite(data)