


class Pessoa:
    def __init__(self, nome_completo, idade, sexo):
        self.nome_completo = nome_completo
        self.idade = idade
        self.sexo = sexo

    @classmethod
    def genero_outro(cls, nome_completo, sexo):
        return cls(nome_completo, 22, sexo) 


p1 = Pessoa.genero_outro('Silvano', 'Masculino')

print(p1.idade)
print(p1.sexo)
print(p1.nome_completo)