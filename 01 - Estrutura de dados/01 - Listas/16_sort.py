linguagens = ["python", "js", "c", "java", "csharp"]

# ORGANIZA LISTA ORDEM ALFABETO
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
# REVERSE = ORDENA DE TRAS PARA FRENTE 
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
# LAMBDA FUNÇÃO ANONIMA
# LEN = TAMANHO DE CADA ITEM QUANTOS TEM
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

# COLOCAR DA QUANTIDADE MAIOR DE ELEMENTOS PARA MENOR SEM ORDEM ALFABETICA
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
