class Cliente:
    def __init__(self, nome, CPF, RG, telefone, email, renda, depinicial, saldo=0):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.depinicial = depinicial
        self.saldo = saldo

    def getCliente(self):
        return self.nome, self.CPF, self.RG, self.telefone, self.email, self.renda, self.depinicial, self.saldo

    def setNome(self, x):
        self.nome = x

    def setCPF(self, x):
        self.CPF = x

    def setRG(self, x):
        self.RG = x

    def setTelefone(self, x):
        self.telefone = x

    def setEmail(self, x):
        self.email = x

class ag:
    def __init__(self):
        self._clientes = {}

    def novo_cliente(self, cliente):
        self._clientes[cliente.nome] = cliente
        print(f"{cliente.nome} foi adicionado")

    def excluir_cliente(self, nome):
        if nome in self._clientes:
            del self._clientes[nome]
            print(f"O cliente {nome} foi excluído")
        else:
            print("Cliente não encontrado")

    def buscar_cliente(self, nome):
        return self._clientes.get(nome, None)


class Transferencia:
    def __init__(self, cliente, saldo):
        self._cliente = cliente
        self._saldo = saldo
        self._enviado = 0
        self._recebido = 0

    def deposito(self, valor):
        self._saldo += valor
        self._recebido += valor

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._enviado += valor
        else:
            print("Saldo Insuficiente")

    def detalhes(self):
        print(f'Cliente: {self._cliente.nome}\nSaldo: {self._saldo}')
        if self._enviado > 0:
            print(f"Sua transferência foi enviada! - {self._enviado}")
        if self._recebido > 0:
            print(f"Sua transferência foi recebida! - {self._recebido}")
        print()



