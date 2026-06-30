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
            "DELETE FROM Matematica WHERE aluno_id = %s",
            (aluno_id,)
            )
            executar(
            "DELETE FROM Portugues WHERE aluno_id = %s",
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
        if resultado:
            executar(
            "DELETE FROM Matematica WHERE aluno_id = %s",
            (aluno_id,)
            )
            situacaomat = "PENDENDE"
            sql = """
            UPDATE Aluno
            SET situacao_mat = %s 
            WHERE id = %s
            """
            valores = (situacaomat, aluno_id)
            executar(sql, valores)
            print("Aluno removido com sucesso.")
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
        if resultado:
            executar(
            "DELETE FROM Portugues WHERE aluno_id = %s",
            (aluno_id,)
            )
            situacaopor = "PENDENDE"
            sql = """
            UPDATE Aluno
            SET situacao_por = %s 
            WHERE id = %s
            """
            valores = (situacaopor, aluno_id)
            executar(sql, valores)
            print("Aluno removido com sucesso.")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)