from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
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
                return redirect(url_for('views.user_managemant'))
            else:
                print('entrou no else')
    return render_template("login.html")

@auth.route('/register', methods=['GET','POST','PUT','DELETE'])
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

@auth.route('/user_management', methods=['GET','POST'])
def user_management():
    if request.method == 'GET':
        print('entrou no post user_management')
        sql = "SELECT NR_SEQUENCIA,NM_USUARIO,NM_PRIMEIRO_NOME,NM_ULTIMO_NOME,DS_EMAIL FROM USERS  ORDER BY 1 ASC"
        json_list = connection.list_users(sql)
        #return json_list
        #print(json_list)
    return render_template("user_management.html", json_list=json_list)

@auth.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if request.method == 'DELETE':
        print('entrou no delete:',id)
    return render_template("user_management.html")
            
@auth.route('/user/<int:id>', methods=['PUT'])
def edit_user(id):
    if request.method == 'PUT':
        print('entrou no put:',id)
        return jsonify({"mensagem": f"Usuário com ID {id} atualizado com sucesso"})
    return render_template("user_management.html")

@auth.route('/search', methods=['GET'])
def search_user():
    if request.method == 'GET':
        search_by = request.args.get('searchBy')
        search_term = request.args.get('searchTerm')
        if (search_by == 'username'):
            userName = search_term
            print('Entrou no if do search term', userName)
            sql = f"SELECT NR_SEQUENCIA,NM_USUARIO,NM_PRIMEIRO_NOME,NM_ULTIMO_NOME,DS_EMAIL FROM USERS WHERE NM_USUARIO = '{userName}'  ORDER BY 1 ASC"
            json_list = connection.list_users(sql)
            print(json_list)
        print('entrou no get search')
    return render_template("user_management.html", json_list=json_list)
