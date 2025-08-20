from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    idade: int


p1 = Pessoa('Silvano', 22)
print(p1)
print(asdict(p1))
print(asdict(p1).items())
print(asdict(p1).keys())
print(asdict(p1).values())
print(astuple(p1))