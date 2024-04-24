clientes = []
usuarios = []
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

# método de listar contas
# método de listar contas por cpf
# método de apagar conta