from cadastrador import cadastrar_aluno
from deletador import *
from leitor import *
from adicionador import *
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
                    lista_alunos()
                elif opcao == "0":
                    print("Até mais...")
                    break
                else:
                    print("Opção inválida!")

        elif usuario == "2":
            senha = input("Qual a senha de professor: ")
            if senha == "123":
                while True:

                    print("\n=== MENU ===")
                    print("1 - Listas")
                    print("2 - Adicionar/Atualizar notas")
                    print("3 - Deletar nota")
                    print("0 - Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        print("1 - Listar alunos")
                        print("2 - Listar notas de matematica")
                        print("3 - Listar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            lista_alunos()
                        elif opcao1 == "2":
                            lista_matematica()
                        elif opcao1 == "3":
                            lista_portugues()
                        else:
                            print("Opção inválida!")

                    elif opcao == "2":
                        print("1 - Adicionar notas de matematica")
                        print("2 - Adicionar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            adicionar_nota_matematica()
                        elif opcao1 == "2":
                            adicionar_nota_portugues()
                        else:
                            print("Opção inválida!")

                    elif opcao == "3":
                        print("1 - Deletar notas de matematica")
                        print("2 - Deletar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            deletar_nota_matematica()
                        elif opcao1 == "2":
                            deletar_nota_portugues()
                        else:
                            print("Opção inválida!")

                    elif opcao == "0":
                        print("Até mais...")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Senha inválida")

        elif usuario == "3":
            senha = input("Qual a senha de administrador: ")
            if senha == ("123"):
                while True:
                    
                    print("\n=== MENU ===")
                    print("1 - Cadastrar aluno")
                    print("2 - Listas")
                    print("3 - Deletar aluno")
                    print("4 - Adicionar/Atualizar notas")
                    print("5 - Deletar nota")
                    print("6 - Editar alunos")
                    print("0 - Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        cadastrar_aluno()
                    elif opcao == "2":
                        print("1 - Listar alunos")
                        print("2 - Listar notas de matematica")
                        print("3 - Listar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            lista_alunos()
                        elif opcao1 == "2":
                            lista_matematica()
                        elif opcao1 == "3":
                            lista_portugues()
                        else:
                            print("Opção inválida!")
                    elif opcao == "3":
                        deletar_aluno()

                    elif opcao == "4":
                        print("1 - Adicionar notas de matematica")
                        print("2 - Adicionar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            adicionar_nota_matematica()
                        elif opcao1 == "2":
                            adicionar_nota_portugues()
                        else:
                            print("Opção inválida!")

                    elif opcao == "5":
                        print("1 - Deletar notas de matematica")
                        print("2 - Deletar notas de portugues ")
                        opcao1 = input("Escolha uma opção: ")
                        if opcao1 == "1":
                            deletar_nota_matematica()
                        elif opcao1 == "2":
                            deletar_nota_portugues()
                        else:
                            print("Opção inválida!")

                    elif opcao == "6":
                        editar_aluno()
                    elif opcao == "0":
                        print("Até mais...")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Senha inválida")
        else:
            print("Opção inválida!")
menu()