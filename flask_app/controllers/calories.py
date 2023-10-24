from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_app.models.calorie import Calorie


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/calculate/calorie')
def addcalories():
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    }
    return render_template('macroCalculator.html',loggedUser = User.get_user_by_id(loggedUserData))

@app.route("/calculate/calorie", methods = ['POST'])
def countCalorie():
    if 'user_id' not in session:
        return redirect('/')
    # if not Calorie.validate_calorie(request.form):
    #     return redirect(request.referrer)
    data = {
        'num': request.form['num'],
        'time': request.form['time'],
        'user_id': session['user_id']
    }   
    Calorie.create_calorie(data)
    return redirect('/')
# @app.route('/calculate/calorie', methods=['POST'])
# def calculate_calorie():
#     if 'user_id' not in session:
#         return redirect('/')

#     # Retrieve data from the form
#     num = request.form.get('num')
#     time = request.form.get('time')

#     data = {
#         'num': num,
#         'time': time,
#         'user_id': session['user_id']
#     }
#     Calorie.create_calorie(data) 

#     flash('Calorie data saved successfully.', 'success')
#     return redirect('/')

from flask import render_template

@app.route('/calculate')
def calculate():
    if 'user_id' not in session:
        return redirect('/')

    loggedUserData = {
        'user_id': session['user_id']
    }

    # Assuming you have the 'loggedUser' and 'calorie' data ready
    loggedUser = User.get_user_by_id(loggedUserData)
    calories = Calorie.get_all(loggedUserData)

    return render_template('macroCalculater.html', loggedUser=loggedUser, calorie=calories)
