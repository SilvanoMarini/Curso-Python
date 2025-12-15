import json
import os


NOME_CAMINHO = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_CAMINHO
    )
)

movie = {
    'title': 'Senhor dos Anéis: A Sociedade dos Anel',
    'original_title': 'The Lord of the Rings: the Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001, 'characters': ['Frodo', 'Sam', 'Gandolf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(movie, arquivo, ensure_ascii=False, indent=2)


with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    str_json = json.load(arquivo)
    print(str_json)

# filme = json.dumps(movie, ensure_ascii=False, indent=2)
# print(filme)