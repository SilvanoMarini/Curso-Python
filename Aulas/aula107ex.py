
def soma_listas(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(soma_listas(lista_a, lista_b))
