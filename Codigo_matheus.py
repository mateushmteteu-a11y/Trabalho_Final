import mysql.connector

def criar_conexão():
    return mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Senac2026",
        database = "Escola",
    )

def cadastrar_aluno():
    nome_do_aluno = input("Nome do aluno")
    