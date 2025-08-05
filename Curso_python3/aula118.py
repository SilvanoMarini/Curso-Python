import json
# caminho_arquivo = 'C:\\Users\\Silva\\OneDrive\\Desktop\\Estudos\\Python\\'
# caminho_arquivo += 'aula186.txt'

# # arqivo = open(caminho_arquivo, 'w')

# # arqivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

# with open(caminho_arquivo, 'r') as arquivo:
#     # print(arquivo.readlines(), end='')
#     # print(arquivo.readline(), end='')
#     # print(arquivo.readline(), end='')
#     print(arquivo.read())
pessoa = {
  "nome": "Luiz Otávio 2",
  "sobrenome": "Miranda",
  "enderecos": [
    {
      "rua": "R1",
      "numero": 32
    },
    {
      "rua": "R2",
      "numero": 55
    }
  ],
  "altura": 1.8,
  "numeros_preferidos": [
    2,
    4,
    6,
    8,
    10
  ],
  "dev": True,
  "nada": None
}

# with open('aula186.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('aula186.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    # for chave, valor in pessoa.items():
    #     print(chave, valor)
    # print(pessoa)
    print(pessoa['nome'])
