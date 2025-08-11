from contas_bancarias import ContaCorrente
from pessoas import Cliente

class Banco():
    def __init__(self):
        self._agencias = [1234, 4321, 3214, 2341]
        self._clientes = []
        self._contas = []

        @property
        def agencias(self):
            return self._agencias


        @agencias.setter
        def agencias(self, agencia: int):
            if agencia not in self._agencias:
                self._agencias.append(agencia)


        def adicionar_cliente(self, nome, idade, cpf, renda, agencia, numero, saldo):
            if agencia not in self._agencias:
                raise ('Agêcia inválida')
            
            cliente = Cliente(nome, idade, cpf, renda)
            conta  = ContaCorrente(agencia, numero )