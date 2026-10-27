import heapq
from itertools import count


class MarketplacePrioritySorter:
    """Fila de prioridade baseada em heapq."""

    def __init__(self):
        self.fila = []
        self.contador = count()

    def criar_item(self, pedido):
        urgencia = pedido.calcular_urgencia()
        atrasado = pedido.prazo <= 0
        return (-int(atrasado), -urgencia, pedido.prazo,
                next(self.contador), pedido)

    def adicionar(self, pedido):
        heapq.heappush(self.fila, self.criar_item(pedido))

    def listar_ordenados(self):
        """Retorna pedidos em ordem de prioridade sem alterar o heap."""
        return [item[4] for item in sorted(self.fila)]

    def mostrar_fila(self, titulo="FILA DE PRIORIDADE"):
        print("\n" + "=" * 88)
        print(titulo)
        print("=" * 88)
        print(f"{'Pos.':<5} {'Pedido':<12} {'Prior.':>7} "
              f"{'Prazo':>8} {'Tam.':>6} {'Urgência':>10} {'Situação':<12}")
        print("-" * 88)
        for posicao, pedido in enumerate(self.listar_ordenados(), start=1):
            if pedido.prazo <= 0:
                situacao = "ATRASADO"
            elif pedido.prazo <= 15:
                situacao = "CRÍTICO"
            elif pedido.prazo <= 60:
                situacao = "ATENÇÃO"
            else:
                situacao = "NO PRAZO"
            print(f"{posicao:<5} {pedido.id_pedido:<12} "
                  f"{pedido.prioridade:>7.0f} {pedido.prazo:>7.0f}m "
                  f"{pedido.tamanho:>6} {pedido.urgencia:>10.2f} {situacao:<12}")

    def explicar_ordem(self):
        print("\nCOMO A FILA É ORDENADA")
        print("1. Pedidos com prazo vencido aparecem primeiro.")
        print("2. Entre eles, vence a maior urgência calculada.")
        print("3. Em empate, vence o menor prazo restante.")
        print("4. Persistindo o empate, vale a ordem de entrada.")
        print("5. O tamanho influencia a fórmula de urgência.")

    def atualizar_tempo(self, minutos):
        if minutos < 0:
            raise ValueError("O tempo não pode ser negativo.")
        pedidos = [item[4] for item in self.fila]
        nova_fila = []
        for pedido in pedidos:
            pedido.prazo -= minutos
            nova_fila.append(self.criar_item(pedido))
        heapq.heapify(nova_fila)
        self.fila = nova_fila
        print(f"\nTempo avançado em {minutos} minutos.")
        print("Todos os pedidos foram recalculados.")

    def despachar(self):
        if not self.fila:
            print("Não existem pedidos na fila.")
            return None
        _, _, _, _, pedido = heapq.heappop(self.fila)
        status = "ATRASADO" if pedido.prazo <= 0 else "DENTRO DO PRAZO"
        print(f"Pedido despachado: {pedido.id_pedido} | "
              f"Urgência: {pedido.urgencia:.2f} | "
              f"Prazo: {pedido.prazo:.0f} min | {status}")
        return pedido
