import unittest
from src.logistica import carregar_pedidos


class TestLogistica(unittest.TestCase):
    def test_carregar_pedidos(self):
        sistema = carregar_pedidos([("A", 50, 20, "P")])
        self.assertEqual(len(sistema.fila), 1)
        self.assertEqual(sistema.listar_ordenados()[0].id_pedido, "A")
