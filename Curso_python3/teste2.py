def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com argumentos {args} e {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorador
def somar(a, b):
    return a + b

print(somar(3, 4))