from abc import ABC, abstractmethod
from random import randint

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
        print(f'✅ Depósito de R${valor:.2f} realizado com sucesso. Novo '
            f'saldo: R${self.saldo:.2f}')


class ContaCorrente(Conta):
    def __init__(self, agencia, titular, saldo):
        super().__init__(agencia, titular, saldo)
        numero_base = ''.join(str(randint(0, 9)) for _ in range(5))

        self.numero = f'{numero_base}-0'
        self.limite_especial = 0.0
        self.debito_limite_especial = 0.0


    def depositar(self, valor):
        if self.debito_limite_especial > 0:
            if valor >= self.debito_limite_especial:
                valor -= self.debito_limite_especial 
                print(f'Débito de R${self.debito_limite_especial} do limite '
                    f'especial quitado')
                self.debito_limite_especial = 0.0
                self.saldo += valor
                if valor > 0:
                    print(f'Depósito de R${valor:.2f} realizado com sucesso.')
                return

            self.debito_limite_especial -= valor
            print(f'Débito do limite especial parcialmente pago. Restante: ' 
                f'R${self.debito_limite_especial:.2f}')

        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')


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
            print(f'✅ Saque de R${valor:.2f} realizado com uso do limite'
                f'especial. Novo saldo: R${self.limite_especial:.2f}')
            return

        print(f'Saldo insuficiente para sacar R${valor:.2f}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, titular, saldo):
        super().__init__(agencia, numero, titular, saldo)
        self.numero = numero + '1'


    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'✅ Saque de R${valor:.2f} realizado com sucesso. Novo '
            f'saldo: R${self.saldo:.2f}')
            return

        print(f'⚠ Saldo insuficiente para sacar R${valor:.2f}. Saldo atual:'
               f'R${self.saldo:.2f}')

