from contas_bancarias import ContaCorrente
from pessoas import Cliente

class Banco():
    def __init__(self):
        self._agencias = {1234, 4321, 3214, 2341}
        self._clientes = []
        self._contas = []
        self._cpfs = set()
        self._numero_contas = set()

    @property
    def agencias(self):
        return self._agencias


    def adicionar_cliente(self, nome, idade, cpf, renda, agencia, saldo):
        if agencia not in self._agencias:
            raise ValueError('Agêcia inválida')
        
        cliente = Cliente(nome, idade, cpf, renda)
        conta  = ContaCorrente(agencia, nome, saldo)

        if cpf in self._cpfs:
            raise ValueError('Cliente já cadastrado')

        if conta.numero in self._numero_contas:
            raise ValueError('Conta já cadastrada')
        
        cliente.contas.append(conta)
        self._clientes.append(cliente)
        self._contas.append(conta)
        self._numero_contas.add(conta.numero)
        self._cpfs.add(cpf)
