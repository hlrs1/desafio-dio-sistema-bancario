menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo =0
limite= 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        while True:
            valor = float(input("Insira o valor para Depósito: "))
            if valor <=0:
                print("Valor inválido. Insira um valor maior que 0!")
            else:
                print(f"Depósito de R$ {valor:.2f} efetuado com Sucesso!")
                saldo += valor
                extrato+= f"Depósito: R$ {valor:.2f}\n"
                break

    elif opcao == "s":
        valor = float (input("Informe o valor do Saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite= valor > limite

        excedeu_saques = numero_saques>=LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Saldo Insuficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação! Limite de saques excedido.")

        elif valor > 0:
            saldo-=valor
            extrato+= f"Saque: R$ {valor:.2f}\n"
            numero_saques+=1
            print(f"Saque de R${valor:.2f} realizado com Sucesso!\n")


    elif opcao == "e":
        
        print("\n===========EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")