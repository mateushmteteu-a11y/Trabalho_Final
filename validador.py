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