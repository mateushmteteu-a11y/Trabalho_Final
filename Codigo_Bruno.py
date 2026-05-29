#LISTA DE ALUNO:
alunos = []

#CALCULAR MÉDIA:
def calcular_média(notas):
    if len(notas) == 0:
        return 0 
    return sum(notas) / len(notas)


#VERIFICAR SITUAÇÃO:
def situação(média):
    if média >= 7.0:
        return "Aprovado"
    elif média >= 5.0:
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

 
 # ADICIONAR NOTAS:
def adicionar_notas():
    listar_alunos()
 
    id_aluno = int(input("Digite o ID do aluno: "))
 
    if id_aluno < 0 or id_aluno >= len(alunos):
        print("Aluno não encontrado.")
        return
 
    quantidade = int(input("Quantas notas deseja adicionar? "))
 
    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i+1}: "))
        alunos[id_aluno]["notas"].append(nota)
 
    print("Notas adicionadas!")


# REMOVER NOTA:
def remover_nota():
    listar_alunos()
 
    id_aluno = int(input("Digite o ID do aluno: "))
 
    if id_aluno < 0 or id_aluno >= len(alunos):
        print("Aluno não encontrado.")
        return
    print(alunos[id_aluno]["notas"])
 
    indice = int(input("Digite o índice da nota: "))
    if indice < 0 or indice >= len(alunos[id_aluno]["notas"]):
        print("Índice inválido.")
        return
    alunos[id_aluno]["notas"].pop(indice)
    print("Nota removida!")
    
 
# MENU
while True:
 
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Editar aluno")
    print("4 - Remover aluno")
    print("5 - Adicionar notas")
    print("6 - Remover nota")
    print("0 - Sair")
 
    opcao = input("Escolha uma opção: ")
 
 
    if opcao == "1":
        cadastrar_aluno()
 
    elif opcao == "2":
        listar_alunos()
 
    elif opcao == "3":
        editar_aluno()
 
    elif opcao == "4":
        remover_aluno()
 
    elif opcao == "5":
        adicionar_notas()
 
    elif opcao == "6":
        remover_nota()
 
    elif opcao == "0":
        print("Sistema encerrado.")
        break
 
    else:
        print("Opção inválida!")
        