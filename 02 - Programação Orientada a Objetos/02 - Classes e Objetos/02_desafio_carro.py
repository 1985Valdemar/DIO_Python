# CRIAR CLASSE E FUNÇÃO PARA REPRESENTAR CARROS

class carro:
    # FAZER CONTRUTOR COM SUAS CARACTERISTICAS
    # SELF REFERENCIA de instancia da caracteristica
    # ATRIBUTO SELF
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    # METODOS = COMPORTAMENTO DO CARRO
    # REFERENCIA EXPLICITA 
        
    def buzinar(self):
        print("BIBIIIII")
        
    def parar(self):
        print("Parando Veiculo")
        print("Veiculo Parado")
        
    def correr(self):
        print("Vrummmmmmmmmm.......")
        
    # DEFINIR METODO DE FORMATAÇÃO PARA IMPRIMIR    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" 
        
# INSTANCIA DE CARRO
# BUSCANDO AS CARACTERISTICAS
carro1 = carro( "Azul", "Fusca", 1970, 1500)
carro1.buzinar()
carro1.parar()
carro1.correr()
# IMPRIMINDO SEM FORMATAÇÃO
print(carro1.cor, carro1.modelo, carro1.ano, carro1.valor)

# IMPRIMINDO COM FORMATAÇÃO DO METODO
carro2 = carro("Bege", "Fusca", 1969, 1500)
print(carro2)

# CHAMANDO SOMENTE METODO ISOLADO
carro2.correr()