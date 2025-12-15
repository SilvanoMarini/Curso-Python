
def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]


capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

zipper(capitais, estados)