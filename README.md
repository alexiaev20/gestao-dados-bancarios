# Gestão de Dados Bancários

Uma aplicação em **Python** para a gestão e processamento eficiente de dados bancários, utilizando técnicas e bibliotecas nativas para análise e gerenciamento de contas e transações.

## 🚀 Funcionalidades
- **Gestão de Contas**: Criação, atualização e exclusão de contas bancárias.
- **Transações**: Registro de saques e depósitos com histórico completo.
- **Relatórios**: Emissão de extrato detalhado por cliente.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Arquitetura**: Orientação a Objetos (POO)
- **Testes**: Unittest nativo

## 📂 Estrutura do Projeto
```text
gestao-dados-bancarios/
├── src/                  # Código fonte principal
│   ├── banco.py          # Lógica do sistema bancário e contas
│   ├── interface.py      # CLI interativa para o usuário
│   ├── main.py           # Ponto de entrada da aplicação
│   └── transacoes.py     # Validações e formatações
├── tests/                # Testes unitários
│   └── test_banco.py     # Testes da classe Banco e ContaBancaria
├── .gitignore
└── README.md
```

## ⚙️ Como Executar
1. Clone o repositório:
```bash
git clone https://github.com/alexiaev20/gestao-dados-bancarios.git
cd gestao-dados-bancarios
```
2. Execute o menu interativo:
```bash
python src/main.py
```
3. Para rodar os testes:
```bash
python -m unittest tests/test_banco.py
```
