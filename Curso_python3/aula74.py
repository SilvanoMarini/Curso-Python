
# def double(a):
#     return a * 2


# def triple(a):
#     return a * 3


# def quadruple(a):
#     return a * 4

# print(f'O dobro de 10 é {double(10)}')
# print(f'O triplo de 10 é {triple(10)}')
# print(f'O quádruplo de 10 é {quadruple(10)}')


def multiply(number):
    def multiple(multiple):
        return number * multiple
    return multiple


numero = multiply(10)
print(numero(4))

