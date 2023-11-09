from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/login')
def link():
    return render_template("login.html")

@auth.route('/register')
def disabled():
    return render_template("register.html")