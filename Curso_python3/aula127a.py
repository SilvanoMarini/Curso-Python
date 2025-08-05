from aula127modulo import salvar


class Pessoa:
    def __init__(self, nome_completo, idade, sexo, estado_civil):
        self.nome_completo = nome_completo
        self.idade = idade
        self.sexo = sexo
        self.estado_civil = estado_civil


dados = [{
    'nome_completo' : 'Silvano Junior Marini Ribeiro',
    'idade' : 22,
    'sexo' : 'Masculino',
    'estado_civil' : 'Solteiro'
},
{
    'nome_completo' : 'Rakel Laiane Oliveira da Silva',
    'idade' : 18,
    'sexo' : 'Feminino',
    'estado_civil' : 'Solteira'
    }]

salvar(dados, 'aula127.json')