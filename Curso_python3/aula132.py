class Caneta:
    # Método construtor, chamado quando cria uma instância da classe
    def __init__(self, marca, cor):
        self.cor_tinta = cor      # A cor da tinta da caneta, inicializada pelo parâmetro
        self.marca = marca        # A marca da caneta, inicializada pelo parâmetro
        self.tamanho = None       # Inicialmente o tamanho é None (sem valor definido)

    # Propriedade (getter) que sempre retorna a cor da tampa como 'Azul' (fixo)
    @property
    def cor_tampa(self):
        return 'Azul'

    # Propriedade (getter) que retorna a cor da tinta da caneta (self.cor_tinta)
    @property
    def cor(self):
        return self.cor_tinta
    
    # Método para definir o tamanho da caneta, recebe um valor e atribui ao atributo tamanho
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    # Setter da propriedade 'cor', permite alterar a cor da tinta da caneta
    @cor.setter
    def cor(self, valor):
        self.cor_tinta = valor


# Criando uma instância da classe Caneta com marca 'Bic' e cor inicial 'Azul'
caneta = Caneta('Bic', 'Azul')

# Definindo o tamanho da caneta como 2.5 usando o método set_tamanho
caneta.set_tamanho(2.5)

# Usando o setter para mudar a cor da tinta para 'Rosa'
caneta.cor = 'Rosa'

# Imprime a cor atual da caneta, que agora é 'Rosa'
print(caneta.cor)

# Imprime o tamanho da caneta, que é 2.5
print(caneta.tamanho)

# Imprime o dicionário interno da instância, mostrando todos os atributos e valores atuais
print(caneta.__dict__)
