import sqlite3
import bcrypt

DB_NAME = "banco.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS contas (
                        cpf TEXT PRIMARY KEY,
                        nome TEXT NOT NULL,
                        senha_hash TEXT NOT NULL,
                        saldo REAL NOT NULL)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cpf TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        valor REAL NOT NULL,
                        FOREIGN KEY(cpf) REFERENCES contas(cpf))''')

def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))
