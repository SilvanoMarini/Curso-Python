import sys
from datetime import datetime

data = datetime.now()
data_real = data.timestamp()
data_agr = datetime.fromtimestamp(data_real)

print(data_agr)

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(f'Quantidade de argumentos {qtd_argumentos}')
print(f'{__file__}')