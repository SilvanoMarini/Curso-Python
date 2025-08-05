class Caneta:
    def __init__(self, marca, cor):
        self.cor_tinta = cor
        self.marca = marca
        self.tamanho = None

    @property
    def cor_tampa(self):
        return 'Azul'

    @property
    def cor(self):
        return self.cor_tinta
    
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    @cor.setter
    def cor(self, valor):
        self.cor_tinta = valor




caneta = Caneta('Bic', 'Azul')
caneta.set_tamanho(2.5)
caneta.cor = 'Rosa'
print(caneta.cor)
print(caneta.tamanho)
print(caneta.__dict__)
