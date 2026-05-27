from leitor import *
from executor import executar
def deletar_aluno():

    try:
        lista_alunos() 
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
        aluno_id = int(input("\nDigite o ID do aluno que deseja deletar a nota: "))
        

        resultado = executar("SELECT * FROM Matematica WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        nome, n1mat, n2mat, n3mat = resultado[0]

        print(f"\nAluno selecionado: {nome}")
        print(f"1 - Nota 1 de matematica (Atual: {n1mat})")
        print(f"2 - Nota 2 de matematica(Atual: {n2mat})")
        print(f"3 - Nota 3 de matematica(Atual: {n3mat})")
        opcao_nota = input("Qual nota você deseja deletar/zerar? (1, 2 ou 3): ")


        if opcao_nota == "1":
            n1mat = 0
            print("Nota 1 de matematica deletada!")
        elif opcao_nota == "2":
            n2mat = 0
            print("Nota 2 de matematica deletada!")
        elif opcao_nota == "3":
            n3mat = 0
            print("Nota 3 de matematica deletada!")
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
        
        sql = """
        UPDATE matematica
        SET nota1_mat = %s, nota2_mat = %s, nota3_mat = %s, soma_mat = %s, media_mat = %s, situacao_mat = %s
        WHERE id = %s
        """
        valores = (n1mat, n2mat, n3mat, somamat, mediamat, situacaomat, aluno_id)
        executar(sql, valores)

        print(f"\nBoletim de {nome} atualizado com sucesso!")
        print(f"Notas atuais de matematica -> Nota1: {n1mat} | Nota2: {n2mat} | Nota3: {n3mat}")
        print(f"Nova Média de matematica: {mediamat:.2f} | Nova Situação de matematica: {situacaomat}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)

def deletar_nota_portugues():

    try:
        lista_portugues()
        aluno_id = int(input("\nDigite o ID do aluno que deseja deletar a nota: "))
        

        resultado = executar("SELECT * FROM Portugues WHERE id = %s", (aluno_id,), fetch=True)
        if not resultado:
            print("Erro: Aluno não encontrado.")
            return

        nome, n1por, n2por, n3por = resultado[0]

        print(f"\nAluno selecionado: {nome}")
        print(f"1 - Nota 1 de portugues(Atual: {n1por})")
        print(f"2 - Nota 2 de portugues(Atual: {n2por})")
        print(f"3 - Nota 3 de portugues(Atual: {n3por})")
        opcao_nota = input("Qual nota você deseja deletar/zerar? (1, 2 ou 3): ")

        if opcao_nota == "1":
            n1por = 0
            print("Nota 1 de portugues deletada!")
        elif opcao_nota == "2":
            n2por = 0
            print("Nota 2 de portugues deletada!")
        elif opcao_nota == "3":
            n3por = 0
            print("Nota 3 de portugues deletada!")
        else:
            print("Opção inválida. Operação cancelada.")
            return

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
        WHERE id = %s
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

        print(f"\nBoletim de {nome} atualizado com sucesso!")
        print(f"Notas atuais de portugues -> Nota1: {n1por} | Nota2: {n2por} | Nota3: {n3por}")
        print(f"Nova Média de : {mediapor:.2f} | Nova Situação de portugues: {situacaopor}")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    except Exception as e:
        print("Erro:", e)