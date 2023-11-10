from flask import Blueprint, render_template, request, flash, redirect, url_for
import cx_Oracle

#with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
#    with connection.cursor() as cursor:
#        sql = """select sysdate from dual"""
#        for r in cursor.execute(sql):
#           print(r)

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

class User():
    def __init__(self):
        self.id
        self.userName
        self.password
        self.firstName
        self.lastName
        self.email
        self.permission




