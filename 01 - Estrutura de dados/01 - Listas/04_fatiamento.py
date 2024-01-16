#  COLCHETE VAI FILTRAR A PARTIR DO NUMERO INDEXAÇÃO INICIAL E FINAL
# [2:] INICIA EM INDEXAÇÃO 2 E VAI ATE FINAL

lista = ["p", "y", "t", "h", "o", "n"]

# INICIA EM 2 E VAI ATE FINAL
print(lista[2:])  # ["t", "h", "o", "n"]

# INICIA E PARA NA iNDEXAÇÃO
print(lista[:2])  # ["p", "y"]

# SELEÇÃO DA INDEXAÇÃO
print(lista[1:3])  # ["y", "t"]

# PULAR DE 2 EM 2
print(lista[0:3:2])  # ["p", "t"]

# IMPRIMIR LISTA SEM CORTES
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# IMPRIMIR DE TRÁS PARA FRENTE
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
