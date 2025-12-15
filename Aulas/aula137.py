
def tabelar(nome1, nome2, nome3, ultimo=False):
    if not ultimo:
        print(f'{nome1:^17} {nome2:^17} {nome3:^17}') 
        return

    print(f'{nome1:^16}| {nome2:^16}| {nome3:^16}|') 


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
        self.motores = []

    def adicionar_motor(self, motor):
        motor.fabricante = self
        self.motores.append(motor)

    def adicionar_carro(self, carro):
        carro.fabricante = self
        self.carros.append(carro)

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.fabricante = None
        self.motor = None
    
    def adicionar_motor(self, motor):
        motor.carros.append(self)
        self.motor = motor


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
        self.fabricante = None

    def adicionar_carro(self, carro):
        carro.motor = self
        self.carros.append(carro)


fabricante1 = Fabricante('BMW')
motor1 = Motor('V8 Aspirado')
carro1 = Carro('BMW 320i')

fabricante1.adicionar_motor(motor1)
fabricante1.adicionar_carro(carro1)
motor1.adicionar_carro(carro1)


fabricante2 = Fabricante('Ford')
carro2 = Carro('Ford Mustang')

fabricante2.adicionar_carro(carro2)
carro2.adicionar_motor(motor1)

carro3 = Carro('BMW M3')
fabricante1.adicionar_carro(carro3)
motor1.adicionar_carro(carro3)

carro4 = Carro('Lamborghini SVJ')
fabricante3 = Fabricante('Lamborghini')
motor2 = Motor('V12 Turbo')

fabricante3.adicionar_carro(carro4)
fabricante3.adicionar_motor(motor2)
carro4.adicionar_motor(motor2)

carros = [carro1, carro2, carro3, carro4]



tabelar('Modelo', 'Motor', 'Fabricante', ultimo='|')
print(53 * '-')

for carro in carros:
    tabelar(carro.nome, carro.motor.nome, carro.fabricante.nome)

print()

# print(motor2.carros[0].nome)
# print(motor2.fabricante.nome)
# for carro in motor1.carros:
#     print(carro.nome, carro.motor.nome)



# for carro in fabricante1.carros:
#     print(carro.nome, carro.motor.nome)


# print(carro2.fabricante.nome)
# print(carro2.motor.fabricante.nome)


# print(carro1.motor.nome)
# print(motor1.fabricante.nome)
# print(motor1.carros[2].nome)


# print(fabricante1.motores[0].carros[0].nome)
# print(fabricante1.carros[0].fabricante.nome)
# print(fabricante1.carros[0].motor.nome)

