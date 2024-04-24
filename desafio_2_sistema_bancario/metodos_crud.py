clientes = []
# cliente1 = {"nome": "Samara", "data de nascimento": "20/08/1997", "cpf": "12345678990", "endereço": "Rua: das Palmeiras, nro 103 - Jardim Prainha - São Paulo/SP"}
# cliente2 = {"nome": "Soraya", "data de nascimento": "20/08/1995", "cpf": "00022255587", "endereço": "Rua: das Palmeiras, nro 103 - Jardim Prainha - São Paulo/SP"}
usuarios = []
# conta1= {'agencia': '0001', 'numero': 1, 'usuario': {'Nome': 'Samara', 'CPF': '12345678990'}, 'saldo': 0, 'limite_por_saque': 500}
# conta2= {'agencia': '0001', 'numero': 2, 'usuario': {'Nome': 'Soraya', 'CPF': '00022255587'}, 'saldo': 0, 'limite_por_saque': 500}
contas = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    nasc = input("Digite a data de nascimento: ")
    cpf = input("Digite o CPF (somente números): ")
    rua = input("Digite o nome da rua do cliente: ")
    numero = input("Digite o número da casa: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input(("Digite a sigla do estado: "))
    endereco = f"Rua: {rua}, nro {numero} - {bairro} - {cidade}/{estado}"
    cliente = {"nome": nome, "data de nascimento": nasc, "cpf": cpf, "endereço": endereco}
    if cliente["cpf"] not in clientes:
        clientes.append(cliente["cpf"])
        usuarios.append(cliente)
        print("Cliente cadastrado com sucesso!")
        return
    else:
        print("Não foi possível cadastrar o cliente. CPF informado já possui um cadastro.")
        return

def cadastrar_conta_corrente(numero, cpf_usuario):
    agencia = '0001'
    user = {}

    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            user = {"Nome": usuario["nome"], "CPF": usuario["cpf"]}
            conta = {"agencia": agencia, "numero": numero, "usuario": user, "saldo": 0, "limite_por_saque": 500}
            contas.append(conta)
            print(f"Conta {numero} cadastrada com sucesso!")
            print(conta)
            usuario_encontrado = True
            break

    if not usuario_encontrado:
        print("Usuário não encontrado")
        return

def listar_contas():
    if len(contas) > 0:
        for conta in contas:
            numero = conta["numero"]
            print(f"Conta {numero}: {conta}")
    else:
        print("Nenhuma conta cadastrada")

def listar_por_cpf(cpf):
    if len(contas) > 0:
        contas_usuario = []

        for conta in contas:
            numero = conta["numero"]
            if conta["usuario"]["CPF"] == cpf:
                contas_usuario.append(conta)

        if len(contas_usuario) > 0:
            for conta_user in contas_usuario:
                print(f"Conta {numero}: {conta_user}")
        else:
            print("Não foram localizadas contas vinculadas ao usuário pesquisado")
    else:
        print("Nenhuma conta cadastrada")

def deletar_conta(num_conta):
    for conta in contas:
        if conta["numero"] == num_conta:
            opcao = 0
            while opcao < 1 or opcao > 2:
                opcao = int(input("Para confirmar digite 1 ou 2 para cancelar "))
                if opcao == 1:
                    contas.remove(conta)
                    print("Conta excluída com sucesso.")
                    return
                elif opcao == 2:
                    return
            break
    else:
        print("Conta não encontrada")
