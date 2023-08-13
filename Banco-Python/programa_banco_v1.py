menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
valor_limite_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    #LÓGICA PARA DEPÓSTIO NA CONTA
    if opcao == "d":
        
        print("DEPÓSITO\n==============")
        
        deposito = float(input("Digite o valor desejado para DEPÓSITAR: "))
        
        if deposito <= 0:
            print("Valor INVÁLIDO para depósito!")
        
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Depósito de R${deposito:.2f} feito com sucesso!")

    #LÓGICA PARA SAQUE NA CONTA
    elif opcao == "s":
        print("SAQUE\n==============")
        saque = float(input("Digite o valor desejado para SACAR: "))

        if saque <= 0:
            print("Valor INVÁLIDO para saque!")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação inválida! Você atingiu o limíte de saques diários!")
        
        elif saque > valor_limite_saque:
            print("Operação inválida! Você só pode sacar no máximo R$500,00 por saque!")
        
        elif saque > saldo:
            print("Operação inválida! Saldo insuficiente!")

        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            print(f"Saque de R${saque:.2f} feito com sucesso!")


    #LÓGICA PARA EXIBIR O EXTRATO DA CONTA
    elif opcao == "e":
        print("EXTRATO")
        print("=============================================\n")

        if extrato == "":
            print("Não houve movimentação!\n")
        else:
            print(extrato)
            print(f"\nSaldo atual: R${saldo:.2f}\n")

        print("=============================================\n")


    #ENCERRA O PROGRAMA
    elif opcao == "q":
        break

    #AVISA AO USUÁRIO CASO ELE ESCOLHA UMA OPÇÃO INEXISTENTE NO MENU
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")