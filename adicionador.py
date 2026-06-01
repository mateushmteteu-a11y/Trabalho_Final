from executor import executar
from leitor import *
from conector import conectar

def adicionar_nota_matematica():
    try:
        lista_alunos()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aluno")
        resultado = cursor.fetchall()
        if not resultado:
            return "Nenhum aluno encontrado."
        else:
            aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))
        
        resultado = executar("SELECT nome, turma FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return
        nome_aluno = resultado[0][0]
        turma_aluno = resultado[0][1]

        print(f"\nAtualizando notas do aluno: {resultado[0][0]}")
        nota1mat = input("Digite a primeira nota de matematica: ")
        nota2mat = input("Digite a segunda nota de matematica: ")
        nota3mat = input("Digite a terceira nota de matematica: ")

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
    
        except ValueError:
            print("Erro: As notas devem ser números.")
            return False
        
        somamat = nota1mat + nota2mat + nota3mat
        mediamat = somamat / 3
        if mediamat >= 7:
            situacaomat = "APROVADO"
        elif mediamat >= 6:
            situacaomat = "RECUPERAÇÃO"
        else:
            situacaomat = "REPROVADO"
        sql = """
            REPLACE INTO Matematica (aluno_id, nome, turma, nota1_mat, nota2_mat, nota3_mat, soma_mat, media_mat, situacao_mat) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (aluno_id, nome_aluno, turma_aluno, nota1mat, nota2mat, nota3mat, somamat, mediamat, situacaomat)
        executar(sql, valores)
        executar("UPDATE Aluno SET situacao_mat = %s WHERE id = %s", (situacaomat, aluno_id))

        print("\nNotas atualizadas com sucesso!")
        print(f"Nova Média de matematica: {mediamat:.2f} | Situação de matematica: {situacaomat}")

    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)

def adicionar_nota_portugues():
    try:
        lista_alunos() 
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aluno")
        resultado = cursor.fetchall()
        if not resultado:
            return "Nenhum aluno encontrado."
        else:
            aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))
        
        resultado = executar("SELECT nome, turma FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return
        nome_aluno = resultado[0][0]
        turma_aluno = resultado[0][1]

        print(f"\nAtualizando notas do aluno: {resultado[0][0]}")
        nota1por = input("Digite a primeira nota de portugues: ")
        nota2por = input("Digite a segunda nota de portugues: ")
        nota3por = input("Digite a terceira nota de portugues: ")

        try:
            nota1por = float(nota1por)
            nota2por = float(nota2por)
            nota3por = float(nota3por)

            if nota1por < 0 or nota1por > 10:
                print("Erro: Nota 1 deve estar entre 0 e 10.")
                return False

            if nota2por < 0 or nota2por > 10:
                print("Erro: Nota 2 deve estar entre 0 e 10.")
                return False

            if nota3por < 0 or nota3por > 10:
                print("Erro: Nota 3 deve estar entre 0 e 10.")
                return False
        except ValueError:
            print("Erro: As notas devem ser números.")
            return False
        
        somapor = nota1por + nota2por + nota3por
        mediapor = somapor / 3
        if mediapor >= 7:
            situacaopor = "APROVADO"
        elif mediapor >= 6:
            situacaopor = "RECUPERAÇÃO"
        else:
            situacaopor = "REPROVADO"
        
        sql = """
            REPLACE INTO Portugues (aluno_id, nome, turma, nota1_por, nota2_por, nota3_por, soma_por, media_por, situacao_por) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (aluno_id, nome_aluno, turma_aluno, nota1por, nota2por, nota3por, somapor, mediapor, situacaopor)
        executar(sql, valores)
        executar("UPDATE Aluno SET situacao_por = %s WHERE id = %s", (situacaopor, aluno_id))

        print("\nNotas atualizadas com sucesso!")
        print(f"Nova Média de portugues: {mediapor:.2f} | Situação de portugues: {situacaopor}")
        
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)
