from random import randint
from contas_bancarias import ContaCorrente, ContaPoupanca
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

    def gerar_numero_conta(self):
        while True:
            numero = ''.join(str(randint(0, 9)) for _ in range(5))
            if numero not in self._numero_contas:
                self._numero_contas.add(numero)
                return numero

    def adicionar_cliente(self, nome, idade, cpf, renda, agencia, saldo=0):
        if agencia not in self._agencias:
            raise ValueError('Agência inválida')

        if cpf in self._cpfs:
            raise ValueError('Cliente já cadastrado')

        numero = self.gerar_numero_conta()
        cliente = Cliente(nome, idade, cpf, renda)
        conta = ContaCorrente(agencia, nome, saldo, numero)

        cliente.contas.append(conta)
        self._clientes.append(cliente)
        self._contas.append(conta)
        self._numero_contas.add(numero)
        self._cpfs.add(cpf)

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta_corrente_do_cliente(self, cliente):
        for conta in cliente.contas:
            if isinstance(conta, ContaCorrente):
                return conta
        return None

    def buscar_conta_poupanca_do_cliente(self, cliente):
        return next((c for c in cliente.contas if isinstance(c, ContaPoupanca)), None)

    def abrir_conta_poupanca(self, cpf):
        cliente = self.buscar_cliente_por_cpf(cpf)
        if not cliente:
            print('Cliente não encontrado')
            return

        conta_corrente = self.buscar_conta_corrente_do_cliente(cliente)
        if not conta_corrente:
            print('Cliente não possui conta corrente')
            return

        # Cria o número da conta poupança baseado na conta corrente
        numero_poupanca = conta_corrente.numero + '-1'

        contapoupanca = ContaPoupanca(
            agencia=conta_corrente.agencia,
            titular=conta_corrente.titular,
            saldo=0,
            numero=numero_poupanca
        )

        cliente.contas.append(contapoupanca)
        self._contas.append(contapoupanca)
        self._numero_contas.add(numero_poupanca)

        print('Conta poupança criada com sucesso!')
