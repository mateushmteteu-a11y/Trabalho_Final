from executor import executar
from leitor import lista

def adicionar_nota_matematica():
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
            UPDATE Matematica
            SET nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s
            WHERE id = %s
            """
            valores = (nota1mat, nota2mat, nota3mat, somamat, mediamat, situacaomat, aluno_id)
            executar(sql, valores)

            sql = """
            UPDATE Aluno
            SET situacao_mat = %s
            WHERE id = %s
            """
            valores = (situacaomat, aluno_id)
            executar(sql, valores)

            print("\nNotas atualizadas com sucesso!")
            print(f"Nova Média de matematica: {mediamat:.2f} | Situação de matematica: {situacaomat}")

    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)

def adicionar_nota_portugues():
    try:
        lista()  
        aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))
        
        resultado = executar("SELECT nome FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

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
        UPDATE Portugues
        SET nota1_por = %s, nota2_por = %s, nota3_por = %s, soma_por = %s, media_por = %s, situacao_por = %s 
        WHERE id = %s
        """
        valores = (nota1por, nota2por, nota3por, somapor, mediapor, situacaopor, aluno_id)
        executar(sql, valores)
        sql = """
        UPDATE Aluno
        SET situacao_por = %s 
        WHERE id = %s
        """
        valores = (nota1por, nota2por, nota3por, somapor, mediapor, situacaopor, aluno_id)
        executar(sql, valores)
        print("\nNotas atualizadas com sucesso!")
        print(f"Nova Média de portugues: {mediapor:.2f} | Situação de portugues: {situacaopor}")
        
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)
