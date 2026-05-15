#LISTA DE ALUNO:
alunos = []

#CALCULAR MÉDIA:
def calcular_média(notas):
    if len(notas) == 0:
        return 0 
    return sum(notas) / len(notas)

#VERIFICAR SITUAÇÃO:
def situação(média):
    if média >= 7:
        return "Aprovado"
    elif média >= 5:
        return "Reprovado"
    else:
        return "reprovado"
    
#CADASTRAR ALUNO:
def cadastrar_aluno():
    nome = input("Nome: ")

    if nome == "":
        print("Nome inválido!")
        return
    
    idade = input("Idade: ")

    if not idade.isdigit():
        print("Idade inválida ")
        return
    
    turma = input("Turma: ")

    aluno = {
        "nome": nome, 
        "idade": idade, 
        "turma": turma,
        "notas": []
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

#LISTAR ALUNOS
def listar_alunos():
    if len(alunos) == 0:
        print("Nunhum aluno cadastrado.")
        return
    
    for i, aluno in enumerate(alunos):

        média = calcular_média(aluno["notas"])
        status = situação(média)