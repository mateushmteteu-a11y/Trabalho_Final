def menu():

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
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                cadastrar_aluno()
            else:
                print("Senha incorreta")

        elif opcao == "2":
            lista()

        elif opcao == "3":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                deletar_aluno()
            else:
                print("Senha incorreta")
                
        elif opcao == "4":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                adicionar_nota()
            else:
                print("Senha incorreta")

        elif opcao == "5":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                deletar_nota()
            else:
                print("Senha incorreta")
        elif opcao == "6":
            senha = input("Digite a senha de funcionario: ")
            if senha == "X-X":
                editar_aluno()
            else:
                print("Senha incorreta")

        elif opcao == "0":
            print("Até mais...")
            break

        else:
            print("Opção inválida!")


menu()