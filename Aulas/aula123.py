from datetime import date


class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, sobrenome, idade=int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def nascimento(self):
        return Pessoa.ano_atual - self.idade
    

# p1 = Pessoa('Silvano', 'Marini', 22)
# # print(p1.idade)
# # print(p1.nascimento())
# # print(Pessoa.ano_atual)
# print(p1.__dict__)
# print(vars(p1))

dados = {'nome' : 'Silvano', 'sobrenome' : 'Marini', 'idade' : 22}
p1 = Pessoa(**dados)
print(vars(p1))