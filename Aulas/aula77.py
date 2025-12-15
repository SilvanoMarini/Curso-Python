

def converter_letra(a):
    return ord(a) - 65


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


print('<<<JOGO DE PERGUNTAS>>>'.center(30, '-'))

for key, value in enumerate(perguntas):
    print(f'Pergunta {key + 1}:')
    print(value['Pergunta'])

    print('ALTERNATIVAS'.center(30, '-'))

    for chave, opcao in enumerate(value['Opções']):
        letra = chr(65 + chave)
        print(f'({letra}) {opcao}')

    while True:
        opcao_validas = ['A', 'B', 'C', 'D']

        resposta = input('Resposta: ').upper().strip()

        if resposta in opcao_validas:
            resposta = converter_letra(resposta)

            if value['Opções'][resposta] == value['Resposta']:
                print('\033[1;32mVocê acertou\033[m')
                break

            else:
                print('\033[1;31mVocê errou\033[m')
                break

        else:
            print('\033[1;31mResposta inválida!!!\033[m')
            continue

    print()
