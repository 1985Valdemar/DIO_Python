# Identação para ficar mais visual e pratico de ler
# METODO SACAR
def sacar(valor): # Inicio do bloco do método
    saldo = 500
#### 4 espaço de identação
    if saldo >= valor: # Inicio do bloco do if
        print("Valor sacado!")
        print("Retire o seu Dinheiro na boca do caixa")
    #### 4 espaço de identação
        saldo -= valor
    print("Obrigado por ser nosso cliente, tenha um Bom Dia!")

sacar(1000)