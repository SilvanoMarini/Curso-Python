import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')


os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        novo_caminho_arquivo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA) , dir_)
        os.makedirs(novo_caminho_arquivo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_caminho_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        # print(novo_caminho_arquivo)
        shutil.copy(caminho_arquivo, novo_caminho_arquivo)
        # print(file)

# print(NOVA_PASTA)