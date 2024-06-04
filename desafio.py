def menu():
    menu ="""\n
    ========== MENU =========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [u] Novo Usuário
    [q] Sair

    => """
    return input(menu)

def sacar(*,saldo,valor, extrato, limite, numero_saques, limite_saques):
        
    excedeu_saldo = valor > saldo

    excedeu_limite= valor > limite

    excedeu_saques = numero_saques>=limite_saques

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
    
    else:
         print(f"Erro! O valor informado é inválido!\n")
    
    return saldo, extrato


def depositar(saldo, valor, extrato,/):
     
    if valor <=0:
        print("Valor inválido. Insira um valor maior que 0!")
    else:
        print(f"Depósito de R$ {valor:.2f} efetuado com Sucesso!")
        saldo += valor
        extrato+= f"Depósito: R$ {valor:.2f}\n"
                       
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n===========EXTRATO============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===============================")

def criar_cliente(clientes):
     cpf= input("Informe o CPF (apenas numeros): ")
     cliente = filtrar_cliente(cpf, clientes)

     if cliente:
          print("\nJá existe usuário com esse CPF!")
          return
    
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

     clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("=== Usuário criado com sucesso! ===")

def filtrar_cliente(cpf, clientes):
    usuarios_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if cliente:
        print("\n *****Conta criada com sucesso!*****")
        return {"agencia":agencia, "numero_conta": numero_conta, "cliente":cliente }
    
    print("\n=====Cliente não encontrado, fluxo de criação de conta encerrado! =====")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(linha)



def main():
    saldo =0
    limite= 500
    extrato =""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":

            valor = float(input("Insira o valor para Depósito: "))
                
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float (input("Informe o valor do Saque: "))
            
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)


        elif opcao == "e":
            
            exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == "n":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                 contas.append(conta)
                 
        elif opcao == "l":
            
            listar_contas(contas)

        elif opcao == "u":
            
            criar_cliente(clientes)

        elif opcao == "q":
            print("""\n    =======================================
    Obrigado por utilizar nossos serviços!
    =======================================\n\n""")
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()