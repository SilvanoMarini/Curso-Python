def somar(x, y):
    """Soma dois números inteiros.

    Parâmetros:
        x (int) -- Primeiro número.
        y (int) -- Segundo número.

    Returna: 
        int: soma dos dois números.
    """
    return x + y


def par_ou_impar(x):
    """Verifica se um número é par ou ímpar.

    Parâmetros:
        x (int) -- Número que será verificado.

    Returna: 
        str: 'Par'se o número for par, 'Ímpar' se o número for ímpar.
    """
    return 'Par' if x % 2 == 0 else 'Ímpar'


def positivo_ou_negativo(x):
    """Verifica se um número é positivo ou negativo

    Parâmetros:
        x (int) -- Número que será verificado

    Returna: 
        str: 'Positivo' se o número for positivo, 'Negativo' se for negativo
    """
    return 'Positivo' if x >= 0 else 'Negativo'


def calcular_imc(peso, altura):
    """Calcula o IMC (Índice de Massa Corporal).

    Parâmetros:
        peso (float): peso em quilogramas.
        altura (float): altura em metros.

    Retorna:
        float: valor do IMC calculado (peso dividido pela altura ao quadrado).
    """
    return peso / (altura ** 2)


def classificacao_imc(imc):
    """Classifica o (IMC) -- índece de massa corporal

    Parâmetros:
        imc (float) -- (IMC) para a classificação


    Returna: 
        str: 
            'Abaixo do peso'   -- (IMC) Abaixo de 18.5
            'Peso normal'      -- (IMC) 18.5 a 24.9
            'Sobrepeso'        -- (IMC) 25.0 a 29.9
            'Obesidade grau 1' -- (IMC) 30.0 a 34.9
            'Obesidade grau 2' -- (IMC) 35.0 a 39.9
            'Obesidade grau 3' -- (IMC) 40.0 ou mais
    """
    if imc < 18.5:
        return 'Abaixo do peso'

    elif imc <= 24.9:
        return 'Peso normal'

    elif imc <= 29.9:
        return 'Sobrepeso'

    elif imc <= 34.9:
        return 'Obesidade grau 1'

    elif imc <= 39.9:
        return 'Obesidade grau 2'

    else:
        return 'Obesidade grau 3'