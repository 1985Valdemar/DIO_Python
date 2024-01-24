class Pessoa:
    # CONSTRUTOR INICIALIZAR
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    # TRANSFERINDO METODO PARA PROPRIEDADE
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento

# PESSOA instancia PESSOA
pessoa = Pessoa("Valdemar", 1985)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
