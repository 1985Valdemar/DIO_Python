linguagens = ["python", "js", "c", "java", "csharp"]

# ORDENA EM LISTA
# MAIOR DIFERENÇA ELE E UMA FUNÇÃO
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
