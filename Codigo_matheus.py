import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Senac2026",
        database = "Escola",
    )

def executar(sql, params=None, fetch=False):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(sql, params or ())

    if fetch:
        resultado = cursor.fetchall()
    else:
        resultado = None

    conexao.commit()
    conexao.close()
    return resultado

def cadastrar_aluno():

    nome = input("Nome do cliente: ")
    executar("INSERT INTO clientes (nome) VALUES (%s)", (nome,))

    idade = int(input("Digite a idade do aluno: "))
    executar("INSERT INTO clientes (idade) VALUES (%s)", (idade,))

    turma = int(input("Digite a turma do aluno: "))
    executar("INSERT INTO clientes (turma) VALUES (%s)", (turma,))


    nota = float(input("Digite a nota do aluno: "))
    executar("INSERT INTO clientes (nota) VALUES (%s)", (nota,))

    print("Cliente cadastrado")

print 