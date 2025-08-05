from aula127modulo import ler, Pessoa

pessoas = ler('aula127.json')

p1 = pessoas[0]

print(p1['nome_completo'])

# for dic in pessoas:
#     for chave, valor in dic.items():
#         print(f"{str(chave).capitalize()}: {valor}")
#     print()
# mostrar = [f"{str(chave).capitalize()}: {pessoa}" for chave, pessoa in pessoas.items()]
# print(*mostrar, sep='\n')
# # print(', '.join(mostrar) + '.')
# print(*[f'{str(chave).capitalize()}: {pessoa}' for chave, pessoa in pessoas.items()], sep='\n')
# for chave, valor in pessoas.items():
#     print(f"{str(chave).capitalize()}: {valor}")

# p1 = Pessoa(**pessoas)

# # print(vars(p1))



# for chave, valor in vars(p1).items():
#     print(f"{str(chave.replace('_', ' ')).capitalize()}: {valor}")
