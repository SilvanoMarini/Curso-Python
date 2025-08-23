import os
import shutil
from pathlib import Path
from zipfile import ZipFile


CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivo_compactado.zip'
CAMINHO_DESCOMPACTADO =  CAMINHO_RAIZ / 'arquivo_descompactado'

Path.mkdir(CAMINHO_ZIP_DIR, exist_ok=True)
# print()

def criar_arquivos(qtd: int, Dir: Path):
    for i in range(qtd):
        texto = f'arquivo_{i + 1}'
        with open(Dir / f'{texto}.txt', 'w' ) as arquivo:
            arquivo.write(f'{texto.capitalize()}\n'
                          f'\nTexto de exemplo')


criar_arquivos(10, CAMINHO_ZIP_DIR)