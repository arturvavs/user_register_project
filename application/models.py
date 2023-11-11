from flask import Blueprint, render_template, request, flash, redirect, url_for
import cx_Oracle
import json

class Conexao():
    def __init__(self):
        self.un = 'SYSTEM'
        self.cs = '127.0.0.1:1521/XE'
        self.pw = 'root'
        self.connection = None
        self.sql = None
         
    def user_login(self,sql):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        if connection:
            try:  
                print('conectado')
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchone()
                    for row in rows:
                        return rows[0]
            except cx_Oracle.Error as error:
                print('Erro ao executar funcao:', error)
                return None
            
    def user_register(self,sql):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        if connection:
            try:  
                print('conectado')
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
                    flash('Account created!', category='success')
            except cx_Oracle.Error as error:
                print('Erro ao executar user_register:', error)
                flash('Error creating account: ' + str(error), category='error')
                return None
            
    def list_users(self,sql):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchall() 
                    users = [] 
                    for row in rows:
                        users.append({
                            'nr_sequencia': row[0],
                            'nm_primeiro_nome': row[1], 
                            'nm_ultimo_nome': row[2],
                            'nm_usuario': row[3],
                            'ds_email': row[4]
                        })
                    json_result = json.dumps(users)
                    decoded_result = json.loads(json_result)
            except cx_Oracle.DatabaseError as e:
                flash('Erro ao fazer login: ' + str(e), category='error')
            finally:
                connection.close()
        return decoded_result

    def delete_users(self,userId):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        sql = f"DELETE FROM USERS WHERE NR_SEQUENCIA = {userId}"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
                flash('User deleted!', category='success')
        except cx_Oracle.DatabaseError as error:
            flash('Erro ao fazer login: ' + str(error), category='error')
        return None

#userName = 'admin2'
connection = Conexao()
#connection = cx_Oracle.connect(user=conexao.un, password=conexao.pw, dsn=conexao.cs)
#sql = (f"SELECT NR_SEQUENCIA,NM_USUARIO,NM_PRIMEIRO_NOME,NM_ULTIMO_NOME,DS_EMAIL FROM USERS WHERE NM_USUARIO = '{userName}'  ORDER BY 1 ASC")
#result = connection.list_users(sql)
#print(result)
#with connection.cursor() as cursor:
#    cursor.execute(sql)
#    rows = cursor.fetchall() 
#    users = []
#    for row in rows:
#        users.append({
#        'nr_sequencia': row[0],
#        'nm_primeiro_nome': row[1], 
#        'nm_ultimo_nome': row[2],
#        'nm_usuario': row[3],
#        'ds_email': row[4]
#                        })

#print(users)