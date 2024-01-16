texto = input("Informe um texto: ")
# LAÇO FOR PARA PERCORRER
# CONSTANTE VOGAIS 
# VALORES FIXO POR ISSO TUDO EM MAISCULO
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()