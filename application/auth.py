from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.models import Conexao

auth = Blueprint('auth', __name__)

connection = Conexao()

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print('entrou no metodo post')
        userName = request.form.get('userName')
        passWord = request.form.get('passWord')
        print(userName)
        print(passWord)
        sql = (f"select ds_senha from users where nm_usuario = '{userName}'")
        row = connection.user_login(sql)
        if row:
            print('entrou if row')
            stored_password = row
            if stored_password == passWord:
                print('Entrou da senha validada')
            else:
                print('entrou no else')
    return render_template("login.html")

@auth.route('/register')
def register():
    return render_template("register.html")
