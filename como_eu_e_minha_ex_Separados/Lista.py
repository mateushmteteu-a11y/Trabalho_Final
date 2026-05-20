def lista():

    print("\n=== Lista de Alunos ===")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    
    if not resultado:
        print("Nenhum aluno encontrado.")
    else:
        for linha in resultado:
            print(f"id: {linha[0]} | aluno: {linha[1]} | idade: {linha[2]} | turma: {linha[3]} | nota1: {linha[4]} | nota2: {linha[5]} | nota3: {linha[6]} | soma: {linha[7]} | média: {linha[8]} | situação: {linha[9]}")
    cursor.close()
    conn.close()