# views.py
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/auth/register')
def user_register():
    return render_template("register.html")

@views.route('/login')
def user_login():
    return render_template("login.html")

@views.route('/user_managemant')
def user_managemant():
    return render_template("user_management.html")