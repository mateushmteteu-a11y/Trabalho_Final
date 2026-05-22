from executor import executar
from leitor import lista
from validador import validar

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
        
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
    except Exception as e:
        print("Erro:", e)

