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
        lista()  
        aluno_id = int(input("\nID do aluno que deseja deletar: "))
        executar(
        "DELETE FROM aluno WHERE id = %s",
        (aluno_id,)
        )
        print("Aluno removido com sucesso.")
    except Exception as e:
        print("Erro:", e)


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


def adicionar_nota():
    try:
        lista()  
        aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))
        
        resultado = executar("SELECT nome FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        print(f"\nAtualizando notas do aluno: {resultado[0][0]}")
        nota1 = input("Digite a nova nota 1: ")
        nota2 = input("Digite a nova nota 2: ")
        nota3 = input("Digite a nova nota 3: ")

        if validar("Validando", 18, 1, nota1, nota2, nota3):
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)

            soma = nota1 + nota2 + nota3
            media = soma / 3
            situacao = "APROVADO" if media >= 7 else "REPROVADO"

            sql = """
            UPDATE aluno 
            SET nota1 = %s, nota2 = %s, nota3 = %s, soma = %s, media = %s, situacao = %s 
            WHERE id = %s
            """
            valores = (nota1, nota2, nota3, soma, media, situacao, aluno_id)
            executar(sql, valores)
            
            print("\nNotas atualizadas com sucesso!")
            print(f"Nova Média: {media:.2f} | Situação: {situacao}")
        else:
            print("Falha ao atualizar notas devido a dados inválidos.")

    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)


def deletar_nota():
    """Permite ao usuário escolher uma nota específica para deletar (zerar) e recalcula as médias."""
    try:
        lista()
        aluno_id = int(input("\nDigite o ID do aluno que deseja deletar a nota: "))
        

        resultado = executar("SELECT nome, nota1, nota2, nota3 FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        nome, n1, n2, n3 = resultado[0]

        print(f"\nAluno selecionado: {nome}")
        print(f"1 - Nota 1 (Atual: {n1})")
        print(f"2 - Nota 2 (Atual: {n2})")
        print(f"3 - Nota 3 (Atual: {n3})")
        
        opcao_nota = input("Qual nota você deseja deletar/zerar? (1, 2 ou 3): ")


        if opcao_nota == "1":
            n1 = 0
            print("Nota 1 deletada!")
        elif opcao_nota == "2":
            n2 = 0
            print("Nota 2 deletada!")
        elif opcao_nota == "3":
            n3 = 0
            print("Nota 3 deletada!")
        else:
            print("Opção inválida. Operação cancelada.")
            return


        soma = n1 + n2 + n3
        media = soma / 3
        situacao = "APROVADO" if media >= 7 else "REPROVADO"


        sql = """
        UPDATE aluno 
        SET nota1 = %s, nota2 = %s, nota3 = %s, soma = %s, media = %s, situacao = %s 
        WHERE id = %s
        """
        valores = (n1, n2, n3, soma, media, situacao, aluno_id)
        executar(sql, valores)

        print(f"\nBoletim de {nome} atualizado com sucesso!")
        print(f"Notas atuais -> Nota1: {n1} | Nota2: {n2} | Nota3: {n3}")
        print(f"Nova Média: {media:.2f} | Nova Situação: {situacao}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)

def editar_aluno():
    print("\n=== Editor de Alunos ===")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    resultado = cursor.fetchall()
    
    for linha in resultado:
        if len(linha) == 0:
            print("nenhum aluno encontrado")
        else:
            print(f"id: {linha[0]} | aluno: {linha[1]} | idade: {linha[2]} | turma: {linha[3]} | situação: {linha[9]}")
    a_id = input("Digite o id do aluno a ser editado: ")
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

def menu():

    while True:

        print("\n=== MENU ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Deletar aluno")
        print("4 - Adicionar/Atualizar notas")
        print("5 - Deletar nota")
        print("6 - Editar alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                cadastrar_aluno()
            else:
                print("Senha incorreta")

        elif opcao == "2":
            lista()

        elif opcao == "3":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                deletar_aluno()
            else:
                print("Senha incorreta")
                
        elif opcao == "4":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                adicionar_nota()
            else:
                print("Senha incorreta")

        elif opcao == "5":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                deletar_nota()
            else:
                print("Senha incorreta")
        elif opcao == "6":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                editar_aluno()
            else:
                print("Senha incorreta")

        elif opcao == "0":
            print("Até mais...")
            break

        else:
            print("Opção inválida!")


menu()