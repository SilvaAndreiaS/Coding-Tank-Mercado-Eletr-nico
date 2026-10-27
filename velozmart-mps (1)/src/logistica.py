from .pedido import Pedido
from .fila_prioridade import MarketplacePrioritySorter


def carregar_pedidos(dados):
    """Converte uma sequência de tuplas (id, prioridade, prazo, tamanho) em pedidos."""
    sistema = MarketplacePrioritySorter()
    for item in dados:
        sistema.adicionar(Pedido(*item))
    return sistema
