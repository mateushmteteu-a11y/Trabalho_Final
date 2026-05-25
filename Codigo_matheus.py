from cadastrador import cadastrar_aluno
from deletador import *
from leitor import lista
from adicionador import adicionar_nota
from editor import editar_aluno

def menu():

    while True:

        print("1 - Aluno")
        print("2 - Professor")
        print("3 - Secretario")
        print("0 - Sair")
        usuario = input("Quem é você: ")

        if usuario == "1":
            while True:
            
                print("\n=== MENU ===")
                print("1 - Listar alunos")
                print("0 - Sair")
                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    lista()
                elif opcao == "0":
                    print("Até mais...")
                    break
                else:
                    print("Opção inválida!")

        elif usuario == "2":
            senha = input("Qual a senha de professor: ")
            if senha == "12345":
                while True:
                    print("\n=== MENU ===")
                    print("1 - Listar alunos")
                    print("2 - Adicionar/Atualizar notas")
                    print("3 - Deletar nota")
                    print("0 - Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        lista()
                    elif opcao == "2":
                        adicionar_nota()
                    elif opcao == "3":
                        deletar_nota()
                    elif opcao == "0":
                        print("Até mais...")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Senha inválida")

        elif usuario == "3":
            senha = input("Qual a senha de administrador: ")
            if senha == ("ixi"):
                while True:
                    print("\n=== MENU ===")
                    print("1 - Cadastrar aluno")
                    print("2 - Listar alunos")
                    print("3 - Deletar aluno")
                    print("4 - Adicionar/Atualizar notas")
                    print("5 - Deletar nota")
                    print("6 - Editar alunos")
                    print("0 - Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        cadastrar_aluno()
                    elif opcao == "2":
                        lista()
                    elif opcao == "3":
                        deletar_aluno()
                    elif opcao == "4":
                        adicionar_nota()
                    elif opcao == "5":
                        deletar_nota()
                    elif opcao == "6":
                        editar_aluno()
                    elif opcao == "0":
                        print("Até mais...")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Senha inválida")


menu()