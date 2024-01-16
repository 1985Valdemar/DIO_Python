sorteio = {1, 23}

# ADD = ADICIONAR
sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

# MESMO ELEMENTO SERÁ IGNORADO
sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
