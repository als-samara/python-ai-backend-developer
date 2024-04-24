import time

def deposito( valor, saldo, extrato, /):
    try:
        confirma = input(f"Deseja prosseguir com o depósito de {valor: .2f}? [S / N] ")
        if confirma.upper() == 'N':
            return saldo
        elif confirma.upper() == 'S':
            novo_saldo = saldo + valor
            hora_deposito = time.localtime()
            operacao = f"Depósito | Valor: R${valor: .2f} | Data: {hora_deposito.tm_year}/{hora_deposito.tm_mon}/{hora_deposito.tm_mday}"
            extrato.append(operacao)
            print(f"Depósito de R${valor: .2f} realizado com sucesso!\nSaldo: R${novo_saldo: .2f}")
            return novo_saldo
    except ValueError:
        print("Digite um valor válido")
        return saldo

def saque(*, saldo, valor, extrato, LIMITE_SAQUES, limite_por_saque):
    numero_saques = sum(1 for operacao in extrato if
                                       f"Saque" in operacao and f"{time.localtime().tm_year}/{time.localtime().tm_mon}/{time.localtime().tm_mday}" in operacao)

    if valor <= saldo and valor <= limite_por_saque:
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diário.")
            return saldo
        else:
            novo_saldo = saldo - valor
            hora_saque = time.localtime()
            operacao = f"Saque | Valor: R${valor: .2f} | Data: {hora_saque.tm_year}/{hora_saque.tm_mon}/{hora_saque.tm_mday}"
            extrato.append(operacao)
            print(f"Saque de R${valor: .2f} realizado com sucesso!\nSaldo: R${novo_saldo: .2f}")
            return novo_saldo
    else:
        if valor > saldo:
            print("Você não possui saldo suficiente para realizar essa operação.")
            return saldo
        else:
            print("Valor fora do seu limite por saque. Consulte seu gerente ou app do banco para mais informações.")
            return saldo

def imprimir_extrato(*, extrato):
    if len(extrato) <= 1:
        print("Não foram realizadas movimentações")
    else:
        print('\n'.join(map(str, extrato)))

