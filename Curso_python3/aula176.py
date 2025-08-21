import json
# from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


str_json ='''
{
  "title": "Senhor dos Anéis: A Sociedade dos Anel",
  "original_title": "The Lord of the Rings: the Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandolf", "Legolas", "Boromir"],
  "budget": null
}
'''

movie: Movie = json.loads(str_json)

print(json.dumps(movie, ensure_ascii=False, indent=2))
# movie = json.loads(str_json)
# print(movie)
# print(movie['title'])