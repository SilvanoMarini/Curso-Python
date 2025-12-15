frase = 'Está frase n tem importancia td aq é so pra encheer espaços'\
    .replace(' ', '').lower()

cont = 0
mais_vezes = 0

while cont < len(frase):
    
    contando = frase.count(frase[cont])
    
    if contando > mais_vezes:
        mais_vezes = contando
        letra = frase[cont]

    cont += 1

print(f'A letra que aparece mais vezes é a letra ({letra.upper()}), '
       f'ela aparece {mais_vezes} vezes')
