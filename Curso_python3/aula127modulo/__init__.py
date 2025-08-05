import json


def salvar(dados, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        return json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def ler(caminho):
    try:
        with open(caminho , 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return print('Dados inexistentes')


class Pessoa:
    def __init__(self, nome_completo, idade, sexo, estado_civil):
        self.nome_completo = nome_completo
        self.idade = idade
        self.sexo = sexo
        self.estado_civil = estado_civil