print('<<<<Calculadora>>>>'.center(30))

while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        print('<<<<Escolha o operador>>>>'.center(30))

        print('(1) = +\n(2) = -\n(3) = /\n(4) = x')

        while True:
            op = float(input('Digite o número correspondente ao operador: '))
            if op == 1:
                resultado = n1 + n2
                op = '+'
                break
            elif op == 2:
                resultado = n1 - n2
                op = '-'
                break
            elif op == 3:
                resultado = n1 / n2
                op = '/'
                break
            elif op == 4:
                resultado = n1 * n2
                op = 'x'
                break
            else:
                print('ERRO!!!Digite um operador válido.')

        print(f'{n1} {op} {n2} é {resultado:.2f}')

        while True:
            entrada = input('Deseja continuar calculando?[S/N]: ').strip().upper()

            if entrada == 'S':
                break
            elif entrada == 'N':
                break
            else:
                continue

        if entrada == 'S':
            continue
        else:
            print('<<<<Programa encerrado>>>>'.center(30))
            break
    except:
        print('Desculpe, mas não foi possivel concluir a operação.')
    