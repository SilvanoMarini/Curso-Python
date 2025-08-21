from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideas = caminho_arquivo.parent / 'ideas.txt'

caminho_python3 = caminho_arquivo.parent / 'aula174.py'

home = Path.home()

ideas.touch()
ideas.write_text("Olá mundo!")
# print(ideas.read_text())

print(caminho_python3.read_text())
# ideas.unlink()
# print(ideas)