def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n!!! Operação falhou! O valor informado é inválido. !!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n!!! Operação falhou! Você não tem saldo suficiente. !!!")
    elif excedeu_limite:
        print("\n!!! Operação falhou! O valor do saque excede o limite. !!!")
    elif excedeu_saques:
        print("\n!!! Operação falhou! Número máximo de saques excedido. !!!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n!!! Operação falhou! O valor informado é inválido. !!!")

    return saldo, extrato, numero_saques

def exibir_extrato(*, saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!! Já existe usuário com esse CPF! !!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!! Usuário não encontrado, fluxo de criação de conta encerrado! !!!")
    return None

def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência:\t{conta['agencia']}")
        print(f"C/C:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
    print("=" * 40)

def listar_usuarios(usuarios):
    if not usuarios:
        print("\n!!! Não existem usuários cadastrados! !!!")
        return

    for usuario in usuarios:
        print("=" * 40)
        print(f"Nome:\t\t{usuario['nome']}")
        print(f"CPF:\t\t{usuario['cpf']}")
        print(f"Nascimento:\t{usuario['data_nascimento']}")
        print(f"Endereço:\t{usuario['endereco']}")
    
    print("=" * 40)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = [
        {
            "nome": "Guilherme Arthur",
            "data_nascimento": "10-10-1990",
            "cpf": "12345678900",
            "endereco": "Rua das Flores, 1 - Centro - São Paulo/SP"
        },
        {
            "nome": "Maria Silva",
            "data_nascimento": "20-05-1985",
            "cpf": "98765432100",
            "endereco": "Av. Brasil, 100 - Alvorada - Belo Horizonte/MG"
        }
    ]

    contas = [
        {
            "agencia": "0001",
            "numero_conta": 1,
            "usuario": usuarios[0]
        },
        {
            "agencia": "0001",
            "numero_conta": 2,
            "usuario": usuarios[1]
        }
    ]

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [lu] Listar usuarios
    [nu] Novo usuário
    [q]  Sair
    => """


    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: ")) 

            saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES,)

        elif opcao == "e":
            exibir_extrato(saldo=saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()