contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# REMOVER
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# PESQUISA = NÃO ENCONTRADO
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
