# interface.py

from banco import Banco
from transacoes import formatar_valor

def menu():
    print("\nBem-vindo ao Sistema Bancário")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Emitir Extrato")
    print("5. Sair")

def criar_conta(banco: Banco):
    nome_cliente = input("Digite o nome do titular: ").strip()
    cpf_cliente = input("Digite o CPF do titular: ").strip()
    saldo_inicial = float(input("Digite o saldo inicial: ").strip())
    banco.criar_conta(nome_cliente, cpf_cliente, saldo_inicial)

def realizar_deposito(banco: Banco):
    cpf_cliente = input("Digite o CPF do titular: ").strip()
    valor = float(input("Digite o valor do depósito: ").strip())
    banco.realizar_deposito(cpf_cliente, valor)

def realizar_saque(banco: Banco):
    cpf_cliente = input("Digite o CPF do titular: ").strip()
    valor = float(input("Digite o valor do saque: ").strip())
    banco.realizar_saque(cpf_cliente, valor)

def emitir_extrato(banco: Banco):
    cpf_cliente = input("Digite o CPF do titular: ").strip()
    banco.emitir_extrato(cpf_cliente)

def executar_sistema():
    banco = Banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_conta(banco)
        elif opcao == "2":
            realizar_deposito(banco)
        elif opcao == "3":
            realizar_saque(banco)
        elif opcao == "4":
            emitir_extrato(banco)
        elif opcao == "5":
            print("Obrigado por usar o Sistema Bancário.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_sistema()
