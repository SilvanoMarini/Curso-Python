import copy

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]


# novos_produtos = [
#     {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
#     for produto in produtos

# ]

# # print(*novos_produtos, sep='\n')


# produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda x: x['nome'], reverse=True)

# # print(*produtos_ordenados_por_nome, sep='\n')

# produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda x: x['preco'])

# print(*produtos_ordenados_por_preco, sep='\n')

novos_produtos = sorted(copy.deepcopy(produtos), key=lambda x: x['nome'], reverse=True)
# print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda x: x['preco'])
print(*produtos_ordenados_por_nome, sep='\n')

