
def multiply(*args):
    total = 1
    numeros = args
    for numero in numeros:
        total *= numero
    return total


def even_odd(a):
    return f'O número {a} é par' if a % 2 == 0 else f'O número {a} é ímpar'



print(multiply(4, 4, 4, 4))
print(even_odd(multiply(3, 5, 5, 9)))

