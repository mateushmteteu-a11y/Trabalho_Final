from conector import conectar
def lista():

    print("\n=== Lista de Alunos ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    for aluno in resultado:
        if not resultado:
            print("Nenhum aluno encontrado.")

        else:
            print(f"""ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Turma: {aluno[3]} | Nota 1 de matematica: {aluno[4]} | Nota 2 de matematica: {aluno[5]} | Nota 3 de matematica: {aluno[6]} | Nota 1 de portugues: {aluno[7]} | Nota 2 de portugues: {aluno[8]} | Nota 3 de portugues: {aluno[9]} \nSoma de matematica: {aluno[10]} | Média de matematica: {aluno[11]:.2f} | Situação de matematica: {aluno[12]} | Soma de portugues: {aluno[13]} | Média de portugues: {aluno[14]:.2f} | Situação de portugues: {aluno[15]}
-----------------------------
                """)
    cursor.close()
    conn.close()

