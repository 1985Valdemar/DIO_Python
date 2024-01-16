# Lê o número de casos de teste
num_casos = int(input())

# Loop através dos casos de teste
for _ in range(num_casos):
    # Lê os valores A e B como strings
    A, B = input().split()

    # Verifica se B corresponde aos últimos dígitos de A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")
