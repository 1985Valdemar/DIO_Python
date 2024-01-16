# Estrutura condicionais e de Repetição em Python
#opcao = int(input("Informe uma opção: [1] sacar \n [2] Etrato "))

#if opcao == 1:
 #   valor = float(input("Informe a quantia para o saque: "))
#elif opcao == 2:
 #   print("Exibindo  o Extrato...")
#else:
 #   exit("Opção Inválida")
    
maior_idade = 18

if maior_idade>= 18:
    print("Maior Idade pode Tirar CNH")
else:
    print("Ainda não pode tirar CNH")


# IF ANINHADO
saldo = 500
saque = 951
conta_normal = False
cheque_especial = 450
conta_universitario = False

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= ( saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque")
elif conta_universitario:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")
else:
    print("Sistema não reconheceu tipo conta entrar em contato com Banco tel:634-5656")