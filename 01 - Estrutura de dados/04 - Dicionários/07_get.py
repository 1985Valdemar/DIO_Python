contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError
# PESQUISA CHAVE SE NÃO TIVER RETORNA NONE
resultado = contatos.get("chave")  # None
print(resultado)

# PESQUISA CHAVE E SE NÃO TIVER RETORNA CHAVE EM VAZIO{}
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
