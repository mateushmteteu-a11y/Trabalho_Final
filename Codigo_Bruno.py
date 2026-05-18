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

#LISTAR ALUNOS:
def listar_alunos():
    if len(alunos) == 0:
        print("Nunhum aluno cadastrado.")
        return
    
    for i, aluno in enumerate(alunos):

        média = calcular_média(aluno["notas"])
        status = situação(média) 
        print("\n---------------------")
        print(f"ID: {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Turma: {aluno['turma']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {média:.2f}")
        print(f"Situação: {status}")

#EDITAR ALUNOS:
def editar_aluno():
    listar_alunos()
 
    id_aluno = int(input("Digite o ID do aluno: "))
 
    if id_aluno < 0 or id_aluno >= len(alunos):
        print("Aluno não encontrado.")
        return
 
    alunos[id_aluno]["nome"] = input("Novo nome: ")
    alunos[id_aluno]["idade"] = int(input("Nova idade: "))
    alunos[id_aluno]["turma"] = input("Nova turma: ")
 
    print("Aluno atualizado!")


#REMOVER ALUNOS:
def remover_aluno():
    listar_alunos()
 
    id_aluno = int(input("Digite o ID do aluno: "))
 
    if id_aluno < 0 or id_aluno >= len(alunos):
        print("Aluno não encontrado.")
        return
 
    alunos.pop(id_aluno)
 
    print("Aluno removido!")
 
 