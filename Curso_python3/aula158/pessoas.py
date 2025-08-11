from abc import ABC, abstractmethod
from contas_bancarias import ContaPoupanca

class Pessoa(ABC):
    def __init__(self, nome, idade, cpf):
        super().__init__()
        self._nome = nome
        self._idede = idade
        self._cpf = cpf


    @property
    def nome(self):
        return self._nome


    @property
    def idade(self):
        return self._idede


    @property
    def cpf(self):
        return self._cpf


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, renda):
        super().__init__(nome, idade, cpf)
        self.renda = renda
        self._contas = []

    @property
    def contas(self):
        return self._contas

    @contas.setter
    def adicionar_conta(self, conta):
        from contas_bancarias import Conta
        if not isinstance(conta, Conta):
           raise TypeError("Só é permitido adicionar objetos do tipo Conta.")
        
        if conta in self.contas:
            raise ValueError("Essa conta já está cadastrada para este cliente.")

        self._contas.append(conta)
        conta.titular = self.nome
