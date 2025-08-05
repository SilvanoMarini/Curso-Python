class A:
    def __init__(self, nome):
        self._nome = nome


    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

l = A('maria')
l.nome = 'João'

print(l.nome)