import unittest
from src.fiscal import validar_identificador_pedido, validar_valor


class TestFiscal(unittest.TestCase):
    def test_identificador_valido(self):
        self.assertTrue(validar_identificador_pedido("ORD-001"))

    def test_identificador_invalido(self):
        with self.assertRaises(ValueError):
            validar_identificador_pedido(" ")

    def test_valor_valido(self):
        self.assertTrue(validar_valor(10.5))

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            validar_valor(-1)
