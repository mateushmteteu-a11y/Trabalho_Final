from executor import executar
def cadastrar_aluno():
    try:
        nome = input("Nome do aluno: ")
        if nome.strip() == "":
            print("Erro: Nome não pode ser vazio.")
            return False

        idade = input("Digite a idade do aluno: ")
        if idade.strip() == "":
            print("Erro: Idade não pode ser vazio.")
            return False
        if idade <= 0:
            print("Erro: Idade deve ser maior que 0.")
            return False
        turma = input("Digite a turma do aluno: ")
        if turma.strip() == "":
            print("Erro: Turma não pode ser vazio.")
            return False

        idade = int(idade)
        turma = (turma)
        sql = """
            INSERT INTO aluno
            (nome, idade, turma)
            VALUES (%s, %s, %s)
            """
        executar(sql, (
                nome,
                idade,
                turma,
            ))
    except ValueError:
        print("Falha ao insirir idade ou turma no sistema.")
        return False
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
        

        


        print("\nAluno cadastrado com sucesso!")
        print(f"Soma das notas de matematica: {somamat}")
        print(f"Média final de matematica: {mediamat:.2f}")
        print(f"Situação de matematica: {situacaomat}")
        print(f"Soma das notas: {somapot}")
        print(f"Média final: {mediapot:.2f}")
        print(f"Situação: {situacaopot}")
