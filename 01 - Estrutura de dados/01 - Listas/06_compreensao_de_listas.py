# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# LIST_COMPREENSION = FICA MAIS INXUTA
# NUMERO = RETORNO
# FOR = DECLARARAVEL
# IF = FILTRO 
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
# ELEVA AO QUADRADO
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
