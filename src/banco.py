# banco.py

from transacoes import validar_valor, validar_titular, registrar_transacao, formatar_valor
from typing import Dict

class Cliente:
    def __init__(self, nome: str, cpf: str):
        if not nome or not cpf:
            raise ValueError("Nome e CPF não podem ser vazios.")
        self.nome = nome
        self.cpf = cpf

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self.nome = nome

    def get_cpf(self) -> str:
        return self.cpf

    def set_cpf(self, cpf: str):
        if not cpf:
            raise ValueError("CPF não pode ser vazio.")
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente: Cliente, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.transacoes = []
        registrar_transacao(cliente.get_nome(), "Abertura da conta", saldo_inicial)

    def depositar(self, valor: float):
        try:
            validar_valor(valor)
            self.saldo += valor
            self.adicionar_transacao("Depósito", valor)
            registrar_transacao(self.cliente.get_nome(), "Depósito", valor)
        except ValueError as e:
            print(f"Erro ao realizar depósito: {e}")

    def sacar(self, valor: float):
        try:
            validar_valor(valor)
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente.")
            self.saldo -= valor
            self.adicionar_transacao("Saque", -valor)
            registrar_transacao(self.cliente.get_nome(), "Saque", -valor)
        except ValueError as e:
            print(f"Erro ao realizar saque: {e}")

    def extrato(self):
        print(f"\nExtrato da conta de {self.cliente.get_nome()}:")
        for transacao in self.transacoes:
            print(f"{transacao['descricao']}: {formatar_valor(transacao['valor'])}")
        print(f"Saldo atual: {formatar_valor(self.saldo)}\n")

    def adicionar_transacao(self, descricao: str, valor: float):
        self.transacoes.append({"descricao": descricao, "valor": valor})

class Banco:
    def __init__(self):
        self.contas: Dict[str, ContaBancaria] = {}

    def criar_conta(self, nome_cliente: str, cpf_cliente: str, saldo_inicial: float = 0.0):
        if cpf_cliente in self.contas:
            print("Já existe uma conta com este CPF.")
            return
        try:
            cliente = Cliente(nome_cliente, cpf_cliente)
            self.contas[cpf_cliente] = ContaBancaria(cliente, saldo_inicial)
            print(f"Conta criada para {nome_cliente} com saldo inicial de {formatar_valor(saldo_inicial)}.")
        except ValueError as e:
            print(f"Erro ao criar conta: {e}")

    def realizar_deposito(self, cpf_cliente: str, valor: float):
        try:
            validar_titular(self, cpf_cliente)
            self.contas[cpf_cliente].depositar(valor)
        except ValueError as e:
            print(f"Erro ao realizar depósito: {e}")

    def realizar_saque(self, cpf_cliente: str, valor: float):
        try:
            validar_titular(self, cpf_cliente)
            self.contas[cpf_cliente].sacar(valor)
        except ValueError as e:
            print(f"Erro ao realizar saque: {e}")

    def emitir_extrato(self, cpf_cliente: str):
        try:
            validar_titular(self, cpf_cliente)
            self.contas[cpf_cliente].extrato()
        except ValueError as e:
            print(f"Erro ao emitir extrato: {e}")
