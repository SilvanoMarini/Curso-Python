import os
from time import sleep

lista_de_compras = []

while True:
    try:
        print('[1] Adicionar à lista  [2] Retirar da lista  [3] Ver a lista  [4] Sair')
        acao_Usuario = int(input('Oque você deseja fazer?: '))

        if acao_Usuario == 1:
            add_lista = input('Digite oque deseja adicionar: ')
            lista_de_compras.append(add_lista)
            print(f'O item ({add_lista}) foi adicionado a lista')
            sleep(3)
            os.system('cls')

        elif acao_Usuario == 2:
            try:
                if len(lista_de_compras) == 0:
                    print('<<<Lista vazia>>>'.center(30))
                    sleep(3)
                    os.system('cls')
                    
                else:
                    removido = lista_de_compras.pop(int(input('Digite o índice para remover: ')))
                    print(f'Você removeu ({removido}) da lista.')
                    sleep(3)
                    os.system('cls')


            except:
                print('Esse índice não existe na lista.')
                sleep(2)
                os.system('cls')

        elif acao_Usuario == 3:
            if len(lista_de_compras) > 0:
                print('-' * 30)
                print(f'Ídice {'Nome':>10}')
                print('-' * 30)

                for k, i in enumerate(lista_de_compras):
                    print(f'{k:.<12}{i}')

                print('-' * 30)
            else:
                print('-' * 30)
                print(f'Ídice {'Nome':>10}')
                print('-' * 30)
                print('<<<Lista vazia>>>'.center(30))
                print('-' * 30)

                sleep(3)
                os.system('cls')

        elif acao_Usuario == 4:
            break

        else:
            print('Digite uma opção válida.')
            sleep(3)
            os.system('cls')
            continue

    except:
        print('Digite uma opção válida.')
        sleep(3)
        os.system('cls')

print('<<<Programa encerrado>>>'.center(30))
