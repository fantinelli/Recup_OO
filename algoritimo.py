from classe import *


def main():

    while True:
        try:
            print("+------------------------------------------+ \n | BEM VINDO AO SOFTWARE DO BANCO | \n+------------------------------------------+ \n [1] Cadastrar cliente \n [2] Transferência \n [3] Depositar \n [4] Sacar \n [5] Consultar saldo \n [6] Sair")

            escolha = int(input("> "))

            if escolha == 1:
                print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
                cliente = Cliente()
                ag.novo_cliente(cliente)
            elif escolha == 2:
                print("Realizar Transferência")
                transferencia(ag)
            elif escolha == 3:
                print("Realizar depósito")
                deposito(ag)
            elif escolha == 4:
                print("Sacar")
                sacar(ag)
            elif escolha == 5:
                print("Consultar saldo")
                consultar_saldo(ag)
            elif escolha == 6:
                break
            else:
                print("Opção inválida.")

        except ValueError:
            print('Problema: Digito não correspondente/ Opção Indisponível')




def transferencia(agencia):
    nome_cliente = input("Digite o nome do cliente: ")
    nome_destino = input("Digite o nome do Destinatário: ")
    valor_envio = float(input("Digite o valor a depositar: "))

    cliente_encontrado = agencia.buscar_cliente(nome_cliente)
    if cliente_encontrado:
        cliente_destino = agencia.buscar_cliente(nome_destino)
        if cliente_destino:
            cliente_encontrado.saldo -= valor_envio
            cliente_destino.saldo += valor_envio
            print(f"Transferência de R${valor_envio:.2f} realizada de {cliente_encontrado.nome} para {cliente_destino.nome}")
        else:
            print("Destinatário não encontrado")
    else:
        print("Remetente não encontrado")

def deposito(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do depósito: "))
        cliente.saldo += valor
        print("Depósito realizado com sucesso!")

def sacar(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do saque: "))
        if valor <= cliente.saldo:
            cliente.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")

def consultar_saldo(agencia):
    nome = input("Digite o Nome do cliente: ")
    cliente = agencia.buscar_cliente(nome)
    if cliente:
        print(f"Saldo de {cliente.nome}: R${cliente.saldo:.2f}")
