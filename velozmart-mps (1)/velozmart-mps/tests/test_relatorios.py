import csv
import os
import tempfile
import unittest
from src.pedido import Pedido
from src.relatorios import exportar_fila_csv


class TestRelatorios(unittest.TestCase):
    def test_exportar_csv(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "fila.csv")
            pedido = Pedido("A", 80, 10, "G")
            pedido.calcular_urgencia()
            exportar_fila_csv([pedido], caminho)
            with open(caminho, encoding="utf-8", newline="") as arquivo:
                linhas = list(csv.DictReader(arquivo))
            self.assertEqual(linhas[0]["id_pedido"], "A")
            self.assertEqual(linhas[0]["situacao"], "CRITICO")
