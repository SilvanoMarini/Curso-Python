from pathlib import Path
import csv

caminho_do_arquivo = Path(__file__).parent / 'aula179.csv'


# with open(caminho_do_arquivo, 'r') as arquivo:
#     reader = csv.reader(arquivo)


with open(caminho_do_arquivo, 'r') as arquivo:
    reader = csv.DictReader(arquivo)

    for line in reader:
        print(line)
