from leitor import *
from executor import executar

def deletar_aluno():

    try:
        lista_alunos() 
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aluno")
        resultado = cursor.fetchall()
        
        if not resultado:
            return "Nenhum aluno encontrado."
        else:
            aluno_id = int(input("\nID do aluno que deseja deletar: "))
        resultado = executar("SELECT nome FROM aluno WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return
        if resultado:
            executar(
            "DELETE FROM aluno WHERE id = %s",
            (aluno_id,)
            )
            executar(
            "DELETE FROM Matematica WHERE id = %s",
            (aluno_id,)
            )
            executar(
            "DELETE FROM Portugues WHERE id = %s",
            (aluno_id,)
            )
            print("Aluno removido com sucesso.")

    except Exception as e:
        print("Erro:", e)
def deletar_nota_matematica():
    try:
        lista_matematica()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Matematica")
        resultado = cursor.fetchall()
        if not resultado:
            return "Nenhuma nota encontrada."
        else:
            aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))

        resultado = executar("SELECT * FROM Matematica WHERE aluno_id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        n1mat = 0
        n2mat = 0
        n3mat = 0

        somamat = n1mat + n2mat + n3mat
        mediamat = somamat / 3
        if mediamat >= 7:
            situacaomat = "APROVADO"
        elif mediamat >= 6:
            situacaomat = "RECUPERAÇÃO"
        else:
            situacaomat = "REPROVADO"
        
        sql = """
        UPDATE matematica
        SET nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s
        WHERE aluno_id = %s
        """
        valores = (n1mat, n2mat, n3mat, somamat, mediamat, situacaomat, aluno_id)
        executar(sql, valores)
        sql = """
        UPDATE Aluno
        SET situacao_mat = %s 
        WHERE id = %s
        """
        valores = (situacaomat, aluno_id)
        executar(sql, valores)

        print(f"\nBoletim do aluno atualizado com sucesso!")
        print(f"Notas atuais de matematica -> Nota1: {n1mat} | Nota2: {n2mat} | Nota3: {n3mat}")
        print(f"Nova Média de matematica: {mediamat:.2f} | Nova Situação de matematica: {situacaomat}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)

def deletar_nota_portugues():
    try:
        lista_portugues()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Portugues")
        resultado = cursor.fetchall()
        if not resultado:
            return "Nenhuma nota encontrada."
        else:
            aluno_id = int(input("\nDigite o ID do aluno que deseja atualizar as notas: "))

        resultado = executar("SELECT * FROM Portugues WHERE aluno_id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

       
        n1por = 0 
        n2por = 0
        n3por = 0

        somapor = n1por + n2por + n3por
        mediapor = somapor / 3
        if mediapor >= 7:
            situacaopor = "APROVADO"
        elif mediapor >= 6:
            situacaopor = "RECUPERAÇÃO"
        else:
            situacaopor = "REPROVADO"

        sql = """
        UPDATE portugues 
        SET nota1_pot = %s, nota2_pot = %s, nota3_pot = %s, soma_pot = %s, media_pot = %s, situacao_pot = %s 
        WHERE aluno_id = %s
        """
        valores = (n1por, n2por, n3por, somapor, mediapor, situacaopor, aluno_id)
        executar(sql, valores)
        sql = """
        UPDATE Aluno
        SET situacao_por = %s 
        WHERE id = %s
        """
        valores = (situacaopor, aluno_id)
        executar(sql, valores)

        print(f"\nBoletim do aluno atualizado com sucesso!")
        print(f"Notas atuais de portugues -> Nota1: {n1por} | Nota2: {n2por} | Nota3: {n3por}")
        print(f"Nova Média de : {mediapor:.2f} | Nova Situação de portugues: {situacaopor}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)