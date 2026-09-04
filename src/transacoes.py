# transacoes.py

from typing import Optional

def validar_valor(valor: float):
    """Valida se o valor é maior que zero."""
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

def validar_titular(banco, cpf_cliente: str):
    """Verifica se o titular existe no banco."""
    if cpf_cliente not in banco.contas:
        raise ValueError("Conta não encontrada.")

def formatar_valor(valor: float) -> str:
    """Formata o valor monetário para o padrão de moeda."""
    return f"R$ {valor:.2f}"

def registrar_transacao(titular: str, descricao: str, valor: float, log_file: Optional[str] = None):
    """Registra a transação em um arquivo de log, se especificado."""
    try:
        log_entry = f"{titular} - {descricao}: {formatar_valor(valor)}\n"
        if log_file:
            with open(log_file, 'a') as file:
                file.write(log_entry)
    except IOError as e:
        print(f"Erro ao registrar transação: {e}")
