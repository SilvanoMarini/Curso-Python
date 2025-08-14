from banco import Banco

if __name__ == "__main__":
    banco = Banco()

    banco.adicionar_cliente("Silvano", 22, "12345678900", renda=2500, agencia=1234)
    banco.abrir_conta_poupanca("12345678900")
    cliente = banco.buscar_cliente_por_cpf("12345678900")
    contapoupanca = banco.buscar_conta_poupanca_do_cliente(cliente= cliente)
    if contapoupanca:
        contapoupanca.sacar(100)
    else:
        print("Conta não encontrada.")


