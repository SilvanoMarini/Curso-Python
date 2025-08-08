from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, titular, saldo):
        super().__init__()
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, titular, saldo):
        super().__init__(agencia, numero, titular, saldo)
        self.limite_especial = 0.0
        self.debito_limite_especial = 0.0


    def depositar(self, valor):
        ...

    def sacar(self, valor: int | float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            return

        elif valor <= self.saldo + self.limite_especial:
            restante = valor - self.saldo
            self.saldo = 0.0
            self.debito_limite_especial += restante
            self.limite_especial -= restante
            print(f'Saque de R${valor:.2f} realizado com uso do limite especial.')
            return

        print(f'Saldo insuficiente para sacar R${valor:.2f}')

