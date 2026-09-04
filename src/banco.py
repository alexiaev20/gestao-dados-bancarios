import sqlite3
from src.transacoes import validar_valor, validar_cpf
from src.database import DB_NAME, hash_senha, verificar_senha

class Banco:
    def criar_conta(self, nome: str, cpf: str, senha: str, saldo: float = 0.0):
        if not validar_cpf(cpf):
            raise ValueError("CPF invalido.")
        senha_hash = hash_senha(senha)
        with sqlite3.connect(DB_NAME) as conn:
            try:
                conn.execute("INSERT INTO contas (cpf, nome, senha_hash, saldo) VALUES (?, ?, ?, ?)", (cpf, nome, senha_hash, saldo))
            except sqlite3.IntegrityError:
                raise ValueError("Conta ja existe.")

    def autenticar(self, cpf: str, senha: str):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute("SELECT senha_hash FROM contas WHERE cpf = ?", (cpf,))
            row = cursor.fetchone()
            if not row or not verificar_senha(senha, row[0]):
                raise ValueError("Credenciais invalidas.")

    def depositar(self, cpf: str, valor: float):
        validar_valor(valor)
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("UPDATE contas SET saldo = saldo + ? WHERE cpf = ?", (valor, cpf))
            conn.execute("INSERT INTO transacoes (cpf, tipo, valor) VALUES (?, 'deposito', ?)", (cpf, valor))

    def sacar(self, cpf: str, senha: str, valor: float):
        self.autenticar(cpf, senha)
        validar_valor(valor)
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute("SELECT saldo FROM contas WHERE cpf = ?", (cpf,))
            row = cursor.fetchone()
            if not row or row[0] < valor:
                raise ValueError("Saldo insuficiente.")
            conn.execute("UPDATE contas SET saldo = saldo - ? WHERE cpf = ?", (valor, cpf))
            conn.execute("INSERT INTO transacoes (cpf, tipo, valor) VALUES (?, 'saque', ?)", (cpf, valor))

    def extrato(self, cpf: str, senha: str) -> dict:
        self.autenticar(cpf, senha)
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.execute("SELECT nome, saldo FROM contas WHERE cpf = ?", (cpf,))
            nome, saldo = cursor.fetchone()
            cursor = conn.execute("SELECT tipo, valor FROM transacoes WHERE cpf = ?", (cpf,))
            transacoes = [{"tipo": row[0], "valor": row[1]} for row in cursor.fetchall()]
        return {"nome": nome, "saldo": saldo, "transacoes": transacoes}
