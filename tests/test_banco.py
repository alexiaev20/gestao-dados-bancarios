import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from banco import Banco
from transacoes import formatar_valor, registrar_transacao, validar_valor, validar_titular

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.banco.criar_conta("Alice", "12345678900", 1000)
        self.banco.criar_conta("Bob", "09876543211", 500)

    def test_deposito(self):
        conta = self.banco.contas["12345678900"]
        conta.depositar(200)
        self.assertEqual(conta.saldo, 1200)

    def test_saque(self):
        conta = self.banco.contas["09876543211"]
        conta.sacar(100)
        self.assertEqual(conta.saldo, 400)

    def test_extrato(self):
        conta = self.banco.contas["12345678900"]
        conta.depositar(300)
        conta.sacar(100)
        with self.assertLogs() as log:
            conta.extrato()
        self.assertIn("Abertura da conta", log.output[0])
        self.assertIn("Depósito", log.output[0])
        self.assertIn("Saque", log.output[0])

    def test_criar_conta_duplicada(self):
        with self.assertLogs() as log:
            self.banco.criar_conta("Alice", "12345678900")
        self.assertIn("Já existe uma conta com este titular.", log.output[0])

    def test_valor_negativo(self):
        conta = self.banco.contas["12345678900"]
        with self.assertRaises(ValueError):
            conta.depositar(-100)
        with self.assertRaises(ValueError):
            conta.sacar(-100)

    def test_criar_conta_invalida(self):
        with self.assertRaises(ValueError):
            self.banco.criar_conta("Invalid", "123456789", -500)

    def test_validador_valor(self):
        with self.assertRaises(ValueError):
            validar_valor(-10)

    def test_validador_titular(self):
        with self.assertRaises(ValueError):
            validar_titular(self.banco, "11111111111")

    def test_formatar_valor(self):
        self.assertEqual(formatar_valor(1234.567), "R$ 1234.57")
        self.assertEqual(formatar_valor(0), "R$ 0.00")
        self.assertEqual(formatar_valor(-1234.567), "R$ -1234.57")

    def test_registrar_transacao(self):
        log_file = "test_log.txt"
        conta = self.banco.contas["12345678900"]
        conta.depositar(100)
        conta.sacar(50)
        registrar_transacao("Alice", "Depósito", 100, log_file)
        registrar_transacao("Alice", "Saque", -50, log_file)
        with open(log_file, 'r') as file:
            logs = file.read()
        self.assertIn("Depósito: R$ 100.00", logs)
        self.assertIn("Saque: R$ -50.00", logs)

    def tearDown(self):
        import os
        try:
            os.remove("test_log.txt")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
