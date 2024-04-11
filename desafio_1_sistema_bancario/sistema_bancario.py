import time

menu = """

*********** Escolha uma opção: ***********

               [1] Depósito
               [2] Saque
               [3] Extrato
               [4] Sair

******************************************

=> """

saldo = 0
limite_saque = 500
extrato = ["EXTRATO BANCÁRIO\n"]
saques_dia_atual = 0
LIMITE_SAQUES = 3

while True:
    option = input(menu)

    if option == '1':
        try:
            deposito = input("Digite o valor do depósito: ")
            saldo += int(deposito)
            hora_deposito = time.localtime()
            operacao = f"Depósito | Valor: R${int(deposito): .2f} | Data: {hora_deposito.tm_year}/{hora_deposito.tm_mon}/{hora_deposito.tm_mday}"
            extrato.append(operacao)
        except ValueError:
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
                if int(saque) < saldo:
                    print("Você não possui saldo suficiente para realizar essa operação.")
                else:
                    print("Valor fora do seu limite por saque. Consulte seu gerente ou app do banco para mais informações.")
        except ValueError:
            print("Digite um valor válido")
        input("Pressione qualquer tecla para voltar ao Menu")

    if option == '3':
        print('\n'.join(map(str, extrato)))
        print(f"\nSaldo atual: {saldo:.2f}\n")
        input("Pressione qualquer tecla para voltar ao Menu")

    if option == '4':
        break