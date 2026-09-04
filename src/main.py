# main.py

from banco import Banco
from interface import menu, criar_conta, realizar_deposito, realizar_saque, emitir_extrato

def executar_sistema():
    """Executa o sistema bancário com interação do usuário."""
    banco = Banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

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
