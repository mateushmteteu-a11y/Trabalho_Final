import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="Escola"
    )


def validar(nome, idade, turma, nota1, nota2, nota3):

    if nome.strip() == "":
        print("Erro: Nome não pode ser vazio.")
        return False

    try:
        idade = int(idade)

        if idade <= 0:
            print("Erro: Idade deve ser maior que 0.")
            return False

    except ValueError:
        print("Erro: Idade deve ser um número.")
        return False

    try:
        turma = int(turma)

    except ValueError:
        print("Erro: Turma deve ser um número.")
        return False

    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)

        if nota1 < 0 or nota1 > 10:
            print("Erro: Nota 1 deve estar entre 0 e 10.")
            return False

        if nota2 < 0 or nota2 > 10:
            print("Erro: Nota 2 deve estar entre 0 e 10.")
            return False

        if nota3 < 0 or nota3 > 10:
            print("Erro: Nota 3 deve estar entre 0 e 10.")
            return False

    except ValueError:
        print("Erro: As notas devem ser números.")
        return False

    return True


def executar(sql, params=None, fetch=False):

    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(sql, params or ())
    

    resultado = None

    if fetch:
        resultado = cursor.fetchall()

    conexao.commit()

    cursor.close()
    conexao.close()

    return resultado


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


def deletar_aluno():

    try:

        aluno_id = int(input("ID do aluno: "))

        executar(
            "DELETE FROM clientes WHERE id = %s",
            (aluno_id,)
        )

        print("Aluno removido com sucesso.")

    except Exception as e:
        print("Erro:", e)


def lista():

    print("\n=== Lista de Alunos ===")

    alunos = executar(
        """
        SELECT * FROM clientes
        """,
        fetch=True
    )

    if len(alunos) == 0:

        print("Nenhum aluno cadastrado.")

    else:

        for aluno in alunos:

            print(f"""
ID: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Turma: {aluno[3]}
Nota 1: {aluno[4]}
Nota 2: {aluno[5]}
Nota 3: {aluno[6]}
Soma: {aluno[7]}
Média: {aluno[8]:.2f}
Situação: {aluno[9]}
-----------------------------
""")


def menu():

    while True:

        print("\n=== MENU ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Deletar aluno")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            lista()

        elif opcao == "3":
            deletar_aluno()

        elif opcao == "0":
            print("Até mais...")
            break

        else:
            print("Opção inválida!")


menu()