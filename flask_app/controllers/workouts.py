from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_app.models.calorie import Calorie


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/add/workout", methods = ['POST'])
def createShow():
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
    return redirect('/')