from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.banco import Banco
from src.database import init_db

app = FastAPI(title="Gestao de Dados Bancarios")
banco = Banco()

@app.on_event("startup")
def startup():
    init_db()

class ContaCreate(BaseModel):
    nome: str
    cpf: str
    senha: str
    saldo_inicial: float = 0.0

class Transacao(BaseModel):
    cpf: str
    senha: str
    valor: float

class ExtratoReq(BaseModel):
    cpf: str
    senha: str

@app.post("/contas")
def criar_conta(conta: ContaCreate):
    try:
        banco.criar_conta(conta.nome, conta.cpf, conta.senha, conta.saldo_inicial)
        return {"mensagem": "Conta criada com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/deposito")
def depositar(cpf: str, valor: float):
    try:
        banco.depositar(cpf, valor)
        return {"mensagem": "Deposito realizado."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/saque")
def sacar(req: Transacao):
    try:
        banco.sacar(req.cpf, req.senha, req.valor)
        return {"mensagem": "Saque realizado."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/extrato")
def extrato(req: ExtratoReq):
    try:
        return banco.extrato(req.cpf, req.senha)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
