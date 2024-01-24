class Cachorro:
    # METODO CONSTRUTOR = __INIT__ COM ESTE PARAMETROS
    # PARA INICIAR VALORES DOS ARGUMENTOS
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        # ATRIBUTOS ABAIXO
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    # METODO DESTRUTOR PARA APAGAR
    # ECONOMIZANDO MEMORIA
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")

# METODO FORA DA CLASSE
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

# CHAMANDO A INSTANCIA  CACHORRO
c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

# FORÇANDO RETIRADA CON DESTRUTOR
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

#criar_cachorro()

