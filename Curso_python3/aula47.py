import os
from time import sleep


palavra_secreta = 'Amarelo'.upper()
palavra_cript = len(palavra_secreta) * '*'
tentativas = correto = incorreto = nova_palavra = 0


while True:
    resposta = input('Digite uma letra que está na palavra secreta: ').upper()

    resposta_str = resposta.isalpha()

    if not resposta_str:
        print('Digite somente letras.')
        sleep(0.5)
        os.system('cls')
        continue

    elif len(resposta) > 1:
        print('Digite somente uma letra.')
        sleep(0.5)
        os.system('cls')
        continue

    else:

        if resposta in palavra_secreta:
            print(f'A letra ({resposta.upper()}) está na palavra secreta.')

            indice = [i for i, letra in enumerate(palavra_secreta) if letra == resposta]
            palavra_lista = list(palavra_cript)

            for i in indice:
                palavra_lista[i] = resposta

            nova_palavra = ''.join(palavra_lista)

            palavra_cript = nova_palavra

            print(f'{nova_palavra}')
            tentativas += 1
            correto += 1 

        else:
            print(f'A letra ({resposta.upper()}) não está na palavra secreta')
            incorreto += 1
            tentativas += 1

        if nova_palavra == palavra_secreta:
            print(f'Parabéns você acertou a palavra secreta <<<{palavra_secreta}>>>')
            break

        while True:
            sair = input('Deseja continuar tentando?[S]im ou [N]ão: ').upper().strip()
            sleep(0.5)
            os.system('cls')
            if sair in ('S', 'N'):
                break
            else:
                continue

    if sair == 'S':
        continue
    else:
        break

print(f'Você tentou {tentativas} vezes, acertou {correto} e errou {incorreto}')
sleep(5)
os.system('cls')