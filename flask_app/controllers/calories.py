from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.workout import Workout
from flask_app.models.calorie import Calorie


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)