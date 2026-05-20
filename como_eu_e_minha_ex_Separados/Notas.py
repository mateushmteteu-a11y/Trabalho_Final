nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")


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
            if media >= 7:
                situacao = "APROVADO"
            elif media >= 6:
                situacao = "RECUPERAÇÃO"
            else:
                situacao = "REPROVADO"

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