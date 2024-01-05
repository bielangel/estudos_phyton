def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    return {'nome': nome, 'cpf': cpf}

def cadastrar_conta():
    numero_conta = input("Digite o número da conta: ")
    senha = input("Digite sua senha: ")
    return {'numero_conta': numero_conta, 'senha': senha, 'saldo': 0, 'limite': 500, 'extrato': "", 'numero_saques': 0}

def menu_operacoes():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    =>"""

def realizar_deposito(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito: R${valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def realizar_saque(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta['saldo']
    excedeu_limite = valor > conta['limite']
    excedeu_saques = conta['numero_saques'] >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque: R$ {valor: .2f}\n"
        conta['numero_saques'] += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato(conta):
    print("EXTRATO")
    print("Nenhuma movimentação foi realizada." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")

# Programa principal
LIMITE_SAQUE = 3
usuario = cadastrar_usuario()
conta_bancaria = cadastrar_conta()

while True:
    opcao = input(menu_operacoes())

    if opcao == "d":
        realizar_deposito(conta_bancaria)
    elif opcao == "s":
        realizar_saque(conta_bancaria)
    elif opcao == "e":
        exibir_extrato(conta_bancaria)
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
