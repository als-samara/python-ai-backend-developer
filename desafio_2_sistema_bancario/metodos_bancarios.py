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

# def saque(valor, saldo, extrato):

def imprimir_extrato(*, extrato):
    if len(extrato) <= 1:
        print("Não foram realizadas movimentações")
    else:
        print('\n'.join(map(str, extrato)))

# refactor e modularização do método de saque