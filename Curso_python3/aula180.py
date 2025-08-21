from pathlib import Path
import csv

caminho_do_arquivo = Path(__file__).parent / 'aula180.csv'




lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]


with open(caminho_do_arquivo, 'w') as arquivo:
    nomes_das_colunas = lista_clientes[0].keys()
    writer = csv.DictWriter(arquivo, fieldnames=nomes_das_colunas) 
    writer.writeheader() 

    for clientes in lista_clientes:
        writer.writerow(clientes)