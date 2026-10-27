import unittest
from src.pedido import Pedido
from src.fila_prioridade import MarketplacePrioritySorter


class TestFilaPrioridade(unittest.TestCase):
    def test_pedido_atrasado_vem_primeiro(self):
        fila = MarketplacePrioritySorter()
        fila.adicionar(Pedido("A", 100, 10, "P"))
        atrasado = Pedido("B", 1, 5, "P")
        atrasado.prazo = -1
        fila.adicionar(atrasado)
        self.assertEqual(fila.listar_ordenados()[0].id_pedido, "B")

    def test_despatchar_fila_vazia(self):
        fila = MarketplacePrioritySorter()
        self.assertIsNone(fila.despachar())

    def test_atualizar_tempo(self):
        fila = MarketplacePrioritySorter()
        fila.adicionar(Pedido("A", 50, 20, "P"))
        fila.atualizar_tempo(5)
        self.assertEqual(fila.listar_ordenados()[0].prazo, 15)
