from conector import conectar
def lista_alunos():

    print("\n=== Lista de Alunos ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    if not resultado:
            print("Nenhum aluno encontrado.")
    else:
        for aluno in resultado:
            print(f"""ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Turma: {aluno[3]} | Situação de matematica: {aluno[4]} | Situação de portugues: {aluno[5]}
-----------------------------""")
    cursor.close()
    conn.close()
def lista_matematica():

    print("\n=== Lista de notas de matematica ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Matematica")
    resultado = cursor.fetchall()
    if not resultado:
            print("Nenhuma nota encontrada.")
    else:
        for aluno in resultado:
            print(f"""ID: {aluno[0]} | Nome: {aluno[1]} | Turma: {aluno[2]} | Nota 1 de matematica: {aluno[3]} | Nota 2 de matematica: {aluno[4]} | Nota 3 de matematica: {aluno[5]} | Soma de matematica: {aluno[6]} | Media de matematica: {aluno[7]} | Situação de matematica: {aluno[8]}
-----------------------------
                """)
    cursor.close()
    conn.close()
def lista_portugues():

    print("\n=== Lista de notas de portugues ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Portugues")
    resultado = cursor.fetchall()
    if not resultado:
            print("Nenhum nota encontrada.")
    else:
        for aluno in resultado:
            print(f"""ID: {aluno[0]} | Nome: {aluno[1]} | Turma: {aluno[2]} | Nota 1 de portugues: {aluno[3]} | Nota 2 de portugues: {aluno[4]} | Nota 3 de portugues: {aluno[5]} | Soma de portugues: {aluno[6]} | Media de portugues: {aluno[7]} | Situação de portugues: {aluno[8]}
-----------------------------
                """)
    cursor.close()
    conn.close()