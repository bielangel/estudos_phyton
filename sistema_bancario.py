menu = """"
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
       
       valor = float (input("informe o valor do depósito:"))
       if valor > 0:
            saldo+=valor
            extrato += f"Deposito: R${valor:.2f}\n"
       else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque:"))
        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite
        
        execedeu_saques = numero_saques >= LIMITE_SAQUE
        if execedeu_saldo:
            print("Operação  falhou! Você nao tem saldo suficiente.")
        
        elif execedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif execedeu_saques:
            print("Operação falhou! Numero maximo de saques execedido.")
        
        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques+= 1

        else:
            print("operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print ("EXTRATO")
        print("Nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: RS{saldo:.2f}")

    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opççao invalida, por favor selecione novamente a operação desejada.")
        