import time, metodos_bancarios, metodos_crud

menu = """

*********** Escolha uma opção: ***********

               [1] Depósito
               [2] Saque*
               [3] Extrato
               [4] Cadastrar Cliente
               [5] Cadastrar Conta Corrente
               [6] Listar Todas as Contas***
               [7] Listar Contas do Usuário***
               [8] Deletar Conta***
               [S] Sair

******************************************

=> """

saldo = 0
limite_saque = 500
extrato = ["EXTRATO BANCÁRIO\n"]
saques_dia_atual = 0
LIMITE_SAQUES = 3
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

    if option == '2':
        saque = input("Digite o valor para saque: ")
        try:
            if int(saque) <= saldo and int(saque) <= limite_saque:
                saques_dia_atual = sum(1 for operacao in extrato if
                                       f"Saque" in operacao and f"{time.localtime().tm_year}/{time.localtime().tm_mon}/{time.localtime().tm_mday}" in operacao)
                if saques_dia_atual >= LIMITE_SAQUES:
                    print("Você atingiu o limite de saques diário.")
                else:
                    saldo -= int(saque)
                    hora_saque = time.localtime()
                    operacao = f"Saque | Valor: R${int(saque): .2f} | Data: {hora_saque.tm_year}/{hora_saque.tm_mon}/{hora_saque.tm_mday}"
                    extrato.append(operacao)
            else:
                if int(saque) > saldo:
                    print("Você não possui saldo suficiente para realizar essa operação.")
                else:
                    print("Valor fora do seu limite por saque. Consulte seu gerente ou app do banco para mais informações.")
        except ValueError:
            print("Digite um valor válido")
        input("Pressione qualquer tecla para voltar ao Menu")

    if option == '3':
        metodos_bancarios.imprimir_extrato(extrato=extrato)
        print(f"\nSaldo atual: {saldo: .2f}\n")
        input("Pressione qualquer tecla para voltar ao Menu")

    if option == '4':
        metodos_crud.cadastrar_cliente()
        input("Pressione qualquer tecla para voltar ao Menu")

    if option == '5':
        numero_conta = numero+1
        cpf = input("Para cadastrar a conta, digite o CPF do usuário: ")
        metodos_crud.cadastrar_conta_corrente(numero_conta, cpf)
        numero += 1

        input("Pressione qualquer tecla para voltar ao Menu")

    if option.upper() == 'S':
        break