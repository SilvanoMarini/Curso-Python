from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, titular, saldo):
        super().__init__()
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def exibir_conta(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.limite_especial = None



    def exibir_conta(self):
        return super().exibir_conta()