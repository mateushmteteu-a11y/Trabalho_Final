from executor import executar


def cadastrar_aluno():

    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if all(c.isalpha() or c.isspace() for c in nome):
            break 
        else:
            print("Por favor digite um nome válido (somente letras e espaços)")
            return False
    if nome.strip() == "":
        print("Erro: Nome não pode ser vazio.")
        return False

    idade = input("Digite a idade do aluno: ")
    
    try:
        idade = int(idade)

        if idade <= 0:
            print("Erro: Idade deve ser maior que 0.")
            return False
        
    except ValueError:
        print("Erro: Idade deve ser um número.")
        return False

    turma = input("Digite a turma do aluno: ")
    
    try:
        turma = int(turma)
    except ValueError:
        print("Erro: Turma deve ser um número.")
        return False
    
    situacaomat = "PEDENDE"
    situacaopor = "PEDENDE"

    sql = """
    INSERT INTO aluno
    (nome, idade, turma, situacao_mat, situacao_por)
    VALUES (%s, %s, %s, %s, %s)
    """

    executar(sql, (
            nome,
            idade,
            turma,
            situacaomat,
            situacaopor
             ))
    

    print("\nAluno cadastrado com sucesso!")