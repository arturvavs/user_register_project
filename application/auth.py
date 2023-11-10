from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.models import Conexao
import cx_Oracle
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
                #return redirect(url_for('views.register'))
            else:
                print('entrou no else')
    return render_template("login.html")

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        print('entrou no post register')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        userName = request.form.get('userName')
        userEmail = request.form.get('userEmail')
        passWord = request.form.get('passWord')
        passWord_confirm = request.form.get('passWord_confirm')
        print(firstName,lastName,userName,userEmail,passWord,passWord_confirm)
        sql = (f"insert into users(nr_sequencia,nm_usuario,nm_primeiro_nome,nm_ultimo_nome,ds_email,dt_usuario_rec,ds_senha) values (users_seq.nextval,'{firstName}','{lastName}','{userName}','{userEmail}`',sysdate,'{passWord}')")
        if passWord == passWord_confirm:
            connection.user_register(sql)
            print('user cadastrado')
            return redirect(url_for('views.user_login'))
    return render_template("register.html")

            

