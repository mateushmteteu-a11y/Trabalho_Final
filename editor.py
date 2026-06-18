from conector import conectar
from executor import executar
def editar_aluno():
    print("\n=== Editor de Alunos ===")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    if not resultado:
            return "Nenhum aluno encontrado."
    else:
        for linha in resultado:
            print(f"id: {linha[0]} | aluno: {linha[1]} | idade: {linha[2]} | turma: {linha[3]} | situação de matematica: {linha[4]} | situação de portugues: {linha[5]}")
    
    aluno_id = int(input("Digite o id do aluno a ser editado: "))
    resultado1 = executar("SELECT nome FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
    if not resultado1:
        print("Erro: Aluno não encontrado.")
        return
    while True:
        nome = input("Digite seu nome: ")
        if all(c.isalpha() or c.isspace() for c in nome):
            break 
        else:
            print("Por favor digite um nome válido (somente letras e espaços)")
            
    idade = input("Digite a idade do aluno: ")
    try:
        idade = int(idade)

        if idade <= 0:
            print("Erro: Idade deve ser maior que 0.")
            return False
    except ValueError:
        print("Erro: Idade deve ser um número.")
        return False

    turma = input("Digite a turma do aluno: ")
    try:
        turma = int(turma)
    except ValueError:
        print("Erro: Turma deve ser um número.")
        return False
    
    sql = """
        UPDATE aluno
        SET nome = %s, idade = %s, turma = %s
        WHERE id = %s
        """
    valores = (nome, idade, turma, aluno_id)
    executar(sql, valores)
    cursor.close()
    conn.close()