from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_app.models.calorie import Calorie
#import


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/loginPage')



@app.route('/loginPage')
def loginPage():
    if 'user_id' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/registerPage')
def registerPage():
    if 'user_id' in session:
        return redirect('/')
    return render_template('register.html')


@app.route('/login', methods = ['POST'])
def loginone():
    if 'user_id' in session:
        return redirect('/')
    user = User.get_user_by_email(request.form)
    if not user:
        flash('This email does not exist.', 'emailLogin')
        return redirect(request.referrer)
    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        flash('Your password is wrong!', 'passwordLogin')
        return redirect(request.referrer)
    session['user_id'] = user['id']
    return redirect('/')
    
@app.route('/register', methods= ['POST'])
def register():
    if 'user_id' in session:
        return redirect('/')
    
    
    if User.get_user_by_email(request.form):
        flash('This email already exists. Try another one.', 'emailSignUp')
        return redirect(request.referrer)
    
    if not User.validate_user(request.form):
        return redirect(request.referrer)
    
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        'confirm_password': request.form['confirm_password'],
        'age':request.form['age'],
        'height':request.form['height'],
        'weight':request.form['weight']
    }
    User.create_user(data)
    flash('User succefully created', 'userRegister')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    } 
    loggedUser = User.get_user_by_id(loggedUserData)

    if not loggedUser:
        return redirect('/logout')
    return render_template('dashboard.html', loggedUser = User.get_user_by_id(loggedUserData))

@app.route('/profile')
def addUser():
    loggedUserData = {
        'user_id': session['user_id']
    } 
    loggedUser = User.get_user_by_id(loggedUserData)
    return render_template('profile.html',loggedUser = User.get_user_by_id(loggedUserData))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/calculator')
def calculator():
    loggedUserData = {
        'user_id': session['user_id']
    } 
    loggedUser = User.get_user_by_id(loggedUserData)
    return render_template('macroCalculater.html',loggedUser = User.get_user_by_id(loggedUserData))

@app.route('/login', methods = ['POST'])
def login():
    if 'user_id' in session:
        return redirect('/')
    user = User.get_user_by_email(request.form)
    if not user:
        flash('This email does not exist.', 'emailLogin')
        return redirect(request.referrer)
    if not bcrypt.check_password_hash(user['password'], request.form['password']):
        flash('Your password is wrong!', 'passwordLogin')
        return redirect(request.referrer)
    session['user_id'] = user['id']
    return redirect('/')

@app.route('/workoutHistory')
def workoutHistory():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('workoutHistory.html')