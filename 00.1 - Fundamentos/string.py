curso = "pYtHon"

# Maisculo
print(curso.upper())

# Minusculo
print(curso.lower())

#titulo
print(curso.title())

curso2 = "  PYTHON  "
print(curso2)

# RETIRAR OS ESPAÇOS DOS DOIS LADOS
print(curso2.strip() + ".")

# RETIRA ESPAÇO À ESQUERDA
print(curso2.lstrip() + ".")

# RETIRA ESPAÇO À DIREITA
print(curso2.rstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "*"))
print("-".join(menu))
