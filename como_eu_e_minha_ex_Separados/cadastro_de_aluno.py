def cadastrar_aluno():

    nome = input("Nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    turma = input("Digite a turma do aluno: ")

    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("Digite a terceira nota: ")

    if validar(nome, idade, turma, nota1, nota2, nota3):

        idade = int(idade)
        turma = (turma)

        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)

        soma = nota1 + nota2 + nota3
        media = soma / 3

        if media >= 7:
            situacao = "APROVADO"
        elif media >= 6:
            situacao = "RECUPERAÇÃO"
        else:
            situacao = "REPROVADO"

        sql = """
        INSERT INTO aluno
        (nome, idade, turma, nota1, nota2, nota3, soma, media, situacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, idade, turma, nota1, nota2, nota3, soma, media, situacao)
        executar(sql, valores)

        print("\nAluno cadastrado com sucesso!")
        print(f"Soma das notas: {soma}")
        print(f"Média final: {media:.2f}")
        print(f"Situação: {situacao}")

    else:
        print("Falha no cadastro.")


def editar_aluno():
    print("\n=== Editor de Alunos ===")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    
    for linha in resultado:
        print(f"id: {linha[0]} | aluno: {linha[1]} | idade: {linha[2]} | turma: {linha[3]} | situação: {linha[9]}")
    
    a_id = input("Digite o id do aluno a ser editado: ")
    if not cursor.execute("SELECT * FROM Aluno"):
            print("Erro: Aluno não encontrado.")
            return
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    turma = input("Digite a turma: ")
    sql = """
        UPDATE aluno
        SET nome = %s, idade = %s, turma = %s
        WHERE id = %s
        """
    valores = (nome, idade, turma, a_id)
    executar(sql, valores)
    cursor.close()
    conn.close()