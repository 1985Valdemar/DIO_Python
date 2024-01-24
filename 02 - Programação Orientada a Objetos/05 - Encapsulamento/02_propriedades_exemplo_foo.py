class Foo:
    # CONSTRUTOR E RECEBE VALOR
    def __init__(self, x=None):
        self._x = x
    
    # DECORADOR 
    # ATRIBUTO X ESTÁ PRONTO PARA USO
    @property
    # METODO E TRANSFORMADO EM PROPRIEDADES COM @PROPERTY
    def x(self):
        return self._x or 0

    @x.setter
    # SETTER PARA MODIFICAÇÃO
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        # EXCLUIR X E COLOCAR 0
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
