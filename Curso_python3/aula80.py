
def encontrar_duplicado(lista):
    numeros_vistos = set()
    duplicado = -1

    for numero in lista:
        if numero in numeros_vistos:
            duplicado = numero
            return duplicado
        numeros_vistos.add(numero)
    
    return duplicado







lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

print(encontrar_duplicado(lista_de_listas_de_inteiros[0]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[1]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[2]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[3]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[4]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[5]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[6]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[7]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[8]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[9]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[10]))
print(encontrar_duplicado(lista_de_listas_de_inteiros[11]))

print(encontrar_duplicado([10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]))