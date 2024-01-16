# Não tem NUmero fixo em executar

opcao = -1

while opcao != 0:
    opcao = int(input(" [1] sacar \n [2] Extrato \n [0] Sair \n n°: "))
    
    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o Extrato ...")
    else:
        print("Sair")
        
        
################### WHILE COM BREAK PARA PARAR LOOP ################################        
while True:
    numero = int(input("Adivinhe número de 0 á 10 Digite N°: "))
    
    if numero == 6:
        print("Parabéns Acertou")
        break
    
    print(numero)
