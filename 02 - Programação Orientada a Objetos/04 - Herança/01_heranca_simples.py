# HERDA CARACTERÍSTICAS
#  
# CLASSE BASE
class Veiculo:
    # METODO CONSTRUTOR __INIT__ E CARREGA AS CARACTERISTICAS
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    # METODO COMPORTAMENTO
    def ligar_motor(self):
        print("Ligando o motor")
        
    # METODO FORMATAÇÃO PARA IMPRIMIR
    def __str__(self):
        return f"\n{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# CLASSE FILHA
class Motocicleta(Veiculo):
    pass

# CLASSE FILHA
class Carro(Veiculo):
    pass

# CLASSE FILHA
class Caminhao(Veiculo):
    # METODO CONSTRUTOR INICIAL
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    # METODO FORMATAÇÃO IMPRIMIR
    def esta_carregado(self):
        print(f"\n{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
print(moto, "\n")
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
print(carro, "\n")
carro.ligar_motor()

caminhao = Caminhao("roxo", "gfd-8712", 8, True)
print(caminhao, "\n",)
caminhao.esta_carregado()
