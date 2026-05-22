from validador import validar
from executor import executar
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
