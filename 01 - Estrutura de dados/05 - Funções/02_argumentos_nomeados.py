# DEFININDO ARGUMENTOS PARA CHAMAR
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# PODE CHAMAR SEM SEQUENCIA MAS PODERÁ DAR ERRO
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# MANEIRA MAIS EFICAZ
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# VAI GERAR UM DICIONARIO
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
