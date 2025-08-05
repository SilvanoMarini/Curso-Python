""" try:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        print(f'O {num} é par')
    else:
        print(f'O número {num} é ímpar')

except:
    print('Desculpe, mas você não digitou um número inteiro.')
 """
""" 
try:  
    hora = float(input('Digite a hora: '))

    if 0 <= hora <= 11.59: 
        print('Bom dia!')
    elif 12 <= hora <= 17.59:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Desculpe, mas você não digitou um horário válido.')
 """
""" 
nome = input('Digite seu nome: ')

if len(nome) <= 4 :
    print('Seu nome é curto')
elif len(nome) < 7:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
 """