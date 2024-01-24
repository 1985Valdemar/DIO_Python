# FUNÇÃO ABRINDO BLOCO COM:
def exibir_mensagem():
    print("Olá mundo!")

# FUNÇÃO COM ARGUMENTO NOME
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# AQUI PARA EXECUTAR A DADA FUNÇÃO 
exibir_mensagem()
# TEM QUE COLOCAR ARGUMENTO SE NÃO DARÁ ERRO NO CASO NOME E OBRIGATORIO 
exibir_mensagem_2(nome="Guilherme")
# OPCIONAL COLOCAR NOME
exibir_mensagem_3()
# OBRIGATORIO COLOCAR NOME
exibir_mensagem_3(nome="Chappie")
