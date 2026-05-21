import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="Escola"
    )


def validar(nome, idade, turma, nota1mat, nota2mat, nota3mat, nota1pot, nota2pot, nota3pot):

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
        nota1mat = float(nota1mat)
        nota2mat = float(nota2mat)
        nota3mat = float(nota3mat)

        if nota1mat < 0 or nota1mat > 10:
            print("Erro: Nota 1 deve estar entre 0 e 10.")
            return False

        if nota2mat < 0 or nota2mat > 10:
            print("Erro: Nota 2 deve estar entre 0 e 10.")
            return False

        if nota3mat < 0 or nota3mat > 10:
            print("Erro: Nota 3 deve estar entre 0 e 10.")
            return False
        nota1pot = float(nota1pot)
        nota2pot = float(nota2pot)
        nota3pot = float(nota3pot)

        if nota1pot < 0 or nota1pot > 10:
            print("Erro: Nota 1 deve estar entre 0 e 10.")
            return False

        if nota2pot < 0 or nota2pot > 10:
            print("Erro: Nota 2 deve estar entre 0 e 10.")
            return False

        if nota3pot < 0 or nota3pot > 10:
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

    nota1mat = input("Digite a primeira nota de matematica: ")
    nota2mat = input("Digite a segunda nota de matematica: ")
    nota3mat = input("Digite a terceira nota de matematica: ")
    nota1pot = input("Digite a primeira nota de portugues: ")
    nota2pot = input("Digite a segunda nota de portugues: ")
    nota3pot = input("Digite a terceira nota de portugues: ")

    if validar(nome, idade, turma, nota1mat, nota2mat, nota3mat, nota1pot, nota2pot, nota3pot):

        idade = int(idade)
        turma = (turma)

        nota1mat = float(nota1mat)
        nota2mat = float(nota2mat)
        nota3mat = float(nota3mat)
        nota1pot = float(nota1pot)
        nota2pot = float(nota2pot)
        nota3pot = float(nota3pot)
        somamat = nota1mat + nota2mat + nota3mat
        mediamat = somamat / 3



        if mediamat >= 7:
            situacaomat = "APROVADO"
        elif mediamat >= 6:
            situacaomat = "RECUPERAÇÃO"
        else:
            situacaomat = "REPROVADO"
        somapot = nota1pot + nota2pot + nota3pot
        mediapot = somapot / 3

        if mediapot >= 7:
            situacaopot = "APROVADO"
        elif mediapot >= 6:
            situacaopot = "RECUPERAÇÃO"
        else:
            situacaopot = "REPROVADO"
        sql = """
        INSERT INTO aluno
        (nome, idade, turma, nota1_mat, nota2_mat, nota3_mat, soma_mat, media_mat, situacao_mat, nota1_pot, nota2_pot, nota3_pot, soma_pot, media_pot, situacao_pot)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        executar(sql, (
            nome,
            idade,
            turma,
            nota1mat,
            nota2mat,
            nota3mat,
            somamat,
            mediamat,
            situacaomat,
            nota1pot,
            nota2pot,
            nota3pot,
            somapot,
            mediapot,
            situacaopot,
        ))


        print("\nAluno cadastrado com sucesso!")
        print(f"Soma das notas de matematica: {somamat}")
        print(f"Média final de matematica: {mediamat:.2f}")
        print(f"Situação de matematica: {situacaomat}")
        print(f"Soma das notas: {somapot}")
        print(f"Média final: {mediapot:.2f}")
        print(f"Situação: {situacaopot}")

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
    for aluno in resultado:
        if not resultado:
            print("Nenhum aluno encontrado.")

        else:
            print(f"""ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Turma: {aluno[3]} | Nota 1 de matematica: {aluno[4]} | Nota 2 de matematica: {aluno[5]} | Nota 3 de matematica: {aluno[6]} | Nota 1 de portugues: {aluno[7]} | Nota 2 de portugues: {aluno[8]} | Nota 3 de portugues: {aluno[9]} \nSoma de matematica: {aluno[10]} | Média de matematica: {aluno[11]:.2f} | Situação de matematica: {aluno[12]} | Soma de portugues: {aluno[13]} | Média de portugues: {aluno[14]:.2f} | Situação de portugues: {aluno[15]}
-----------------------------
                """)
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
        nota1mat = input("Digite a primeira nota de matematica: ")
        nota2mat = input("Digite a segunda nota de matematica: ")
        nota3mat = input("Digite a terceira nota de matematica: ")
        nota1pot = input("Digite a primeira nota de portugues: ")
        nota2pot = input("Digite a segunda nota de portugues: ")
        nota3pot = input("Digite a terceira nota de portugues: ")

        if validar(nota1mat, nota2mat, nota3mat, nota1pot, nota2pot, nota3pot):

            nota1mat = float(nota1mat)
            nota2mat = float(nota2mat)
            nota3mat = float(nota3mat)
            nota1pot = float(nota1pot)
            nota2pot = float(nota2pot)
            nota3pot = float(nota3pot)

            somamat = nota1mat + nota2mat + nota3mat
            mediamat = somamat / 3
            if mediamat >= 7:
                situacaomat = "APROVADO"
            elif mediamat >= 6:
                situacaomat = "RECUPERAÇÃO"
            else:
                situacaomat = "REPROVADO"

            somapot = nota1pot + nota2pot + nota3pot
            mediapot = somapot / 3
            if mediapot >= 7:
                situacaopot = "APROVADO"
            elif mediapot >= 6:
                situacaopot = "RECUPERAÇÃO"
            else:
                situacaopot = "REPROVADO"
        
            sql = """
            UPDATE aluno 
            SET nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s, nota1_pot = %s, nota2_pot = %s, nota3_pot = %s, soma_pot = %s, media_pot = %s, situacao_pot = %s 
            WHERE id = %s
            """
            valores = (nota1mat, nota2mat, nota3mat, somamat, mediamat, situacaomat, nota1pot, nota2pot, nota3pot, somapot, mediapot, situacaopot, aluno_id)
            executar(sql, valores)
            
            print("\nNotas atualizadas com sucesso!")
            print(f"Nova Média de matematica: {mediamat:.2f} | Situação de matematica: {situacaomat}")
            print(f"Nova Média de portugues: {mediapot:.2f} | Situação de portugues: {situacaopot}")
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
        

        resultado = executar("SELECT nome, nota1_mat, nota2_mat, nota3_mat, nota1_pot, nota2_pot, nota3_pot FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        nome, n1mat, n2mat, n3mat, n1por, n2por, n3por = resultado[0]

        print(f"\nAluno selecionado: {nome}")
        print(f"1 - Nota 1 de matematica (Atual: {n1mat})")
        print(f"2 - Nota 2 de matematica(Atual: {n2mat})")
        print(f"3 - Nota 3 de matematica(Atual: {n3mat})")
        print(f"4 - Nota 1 de portugues(Atual: {n1por})")
        print(f"5 - Nota 2 de portugues(Atual: {n2por})")
        print(f"6 - Nota 3 de portugues(Atual: {n3por})")
        opcao_nota = input("Qual nota você deseja deletar/zerar? (1, 2, 3, 4, 5 ou 6): ")


        if opcao_nota == "1":
            n1mat = 0
            print("Nota 1 de matematica deletada!")
        elif opcao_nota == "2":
            n2mat = 0
            print("Nota 2 de matematica deletada!")
        elif opcao_nota == "3":
            n3mat = 0
            print("Nota 3 de matematica deletada!")
        elif opcao_nota == "4":
            n1por = 0
            print("Nota 1 de portugues deletada!")
        elif opcao_nota == "5":
            n2por = 0
            print("Nota 2 de portugues deletada!")
        elif opcao_nota == "6":
            n3por = 0
            print("Nota 3 de portugues deletada!")
        else:
            print("Opção inválida. Operação cancelada.")
            return


        somamat = n1mat + n2mat + n3mat
        mediamat = somamat / 3
        if mediamat >= 7:
            situacaomat = "APROVADO"
        elif mediamat >= 6:
            situacaomat = "RECUPERAÇÃO"
        else:
            situacaomat = "REPROVADO"
        somapor = n1por + n2por + n3por
        mediapor = somapor / 3
        if mediapor >= 7:
            situacaopor = "APROVADO"
        elif mediapor >= 6:
            situacaopor = "RECUPERAÇÃO"
        else:
            situacaopor = "REPROVADO"


        sql = """
        UPDATE aluno 
        SET nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s, nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s 
        WHERE id = %s
        """
        valores = (n1mat, n2mat, n3mat, somamat, mediamat, situacaomat, n1por, n2por, n3por, somapor, mediapor, situacaopor, aluno_id)
        executar(sql, valores)

        print(f"\nBoletim de {nome} atualizado com sucesso!")
        print(f"Notas atuais de matematica -> Nota1: {n1mat} | Nota2: {n2mat} | Nota3: {n3mat}")
        print(f"Nova Média de matematica: {mediamat:.2f} | Nova Situação de matematica: {situacaomat}")
        print(f"\nBoletim de {nome} atualizado com sucesso!")
        print(f"Notas atuais de portugues -> Nota1: {n1por} | Nota2: {n2por} | Nota3: {n3por}")
        print(f"Nova Média de : {mediapor:.2f} | Nova Situação de portugues: {situacaopor}")

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
        print(f"id: {linha[0]} | aluno: {linha[1]} | idade: {linha[2]} | turma: {linha[3]} | situação de matematica: {linha[12]} | situação de portugues: {linha[15]}")
    
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