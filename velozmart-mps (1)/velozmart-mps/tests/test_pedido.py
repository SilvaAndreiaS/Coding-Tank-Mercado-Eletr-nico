import unittest
from src.pedido import Pedido


class TestPedido(unittest.TestCase):
    def test_calcular_urgencia(self):
        pedido = Pedido("A1", 90, 30, "M")
        self.assertAlmostEqual(pedido.calcular_urgencia(), 3.6)

    def test_prioridade_invalida(self):
        with self.assertRaises(ValueError):
            Pedido("A1", 101, 30, "P")

    def test_prazo_inicial_negativo(self):
        with self.assertRaises(ValueError):
            Pedido("A1", 50, -1, "P")

    def test_tamanho_invalido(self):
        with self.assertRaises(ValueError):
            Pedido("A1", 50, 30, "X")
