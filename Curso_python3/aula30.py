velocidade = 62
local_carro = 102

RADAR_1 = 60
RADAR_LOCAL = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('O carro utrapassou a velocidade do radar')

if velocidade > RADAR_1 and 101 >= local_carro >= 99:
    print('O carro foi multado no radar')

else:
    print('O carro não foi multado no radar')
