import metodos_bancarios, metodos_crud

menu = """

*********** Escolha uma opção: ***********

               [1] Depósito
               [2] Saque
               [3] Extrato
               [4] Cadastrar Cliente
               [5] Cadastrar Conta Corrente
               [6] Listar Todas as Contas
               [7] Listar Contas do Usuário
               [8] Deletar Conta
               [S] Sair

******************************************

=> """

saldo = 0
extrato = ["EXTRATO BANCÁRIO\n"]
clientes = []
numero = 0


while True:
    option = input(menu)

    if option == '1':
        try:
            deposito = int(input("Digite o valor do depósito: "))
            saldo = metodos_bancarios.deposito(deposito, saldo, extrato)
        except:
            print("Digite um valor válido")

        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '2':
        try:
            saque = int(input("Digite o valor para saque: "))
            saldo = metodos_bancarios.saque(saldo=saldo, valor=saque, extrato=extrato, LIMITE_SAQUES = 3, limite_por_saque = 500)
        except ValueError:
            print("Digite um valor válido")
        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '3':
        metodos_bancarios.imprimir_extrato(extrato=extrato)
        print(f"\nSaldo atual: {saldo: .2f}\n")
        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '4':
        metodos_crud.cadastrar_cliente()
        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '5':
        numero_conta = numero+1
        cpf = input("Para cadastrar a conta, digite o CPF do usuário: ")
        metodos_crud.cadastrar_conta_corrente(numero_conta, cpf)
        numero += 1

        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '6':
        metodos_crud.listar_contas()
        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '7':
        cpf_digitado = input("Digite o CPF do usuário (apenas números): ")
        metodos_crud.listar_por_cpf(cpf_digitado)
        input("Pressione qualquer tecla para voltar ao Menu")

    elif option == '8':
        try:
            numero = int(input("Digite o número da conta a ser apagada: "))
            metodos_crud.deletar_conta(numero)
        except ValueError:
            print("Digite apenas números")
        finally:
            input("Pressione qualquer tecla para voltar ao Menu")

    elif option.upper() == 'S':
        break

    else:
        input("Opção inválida, pressione qualquer tecla para voltar ao Menu")