import random

class Pedido:
    def __init__(self, id_pedido, prioridade, prazo, tamanho):
        self.id_pedido = id_pedido
        self.prioridade = prioridade
        self.prazo = prazo  # Prazo em minutos
        self.tamanho = tamanho
    
    def calcular_indice(self):
        """Avalia o SLA: cruza a prioridade com o tempo restante."""
        if self.prazo <= 0:
            return 99.99 # Prazo estourado recebe índice máximo de urgência
        return round(self.prioridade / self.prazo, 2)

    def obter_situacao(self):
        """Define o status do SLA com base no índice de criticidade."""
        if self.prazo <= 0:
            return "ATRASADO"
        
        indice = self.calcular_indice()
        if indice >= 5.00:
            return "CRÍTICO"
        elif indice >= 2.00:
            return "ATENÇÃO"
        else:
            return "NO PRAZO"

class SimuladorSLA:
    def __init__(self):
        self.fila = []
        self.historico_expedicao = []
        self.tempo_simulado = 0
        
    def carregar_pedidos(self, pedidos):
        print("ETAPA 1 - ENTRADA DOS 40 PEDIDOS")
        for p in pedidos:
            self.fila.append(p)
        print(f"{len(pedidos)} pedidos recebidos e adicionados à fila com sucesso.")
        print("-" * 40)
            
    def repriorizar_fila(self):
        """Ordena a fila do maior índice (mais crítico) para o menor."""
        self.fila.sort(key=lambda p: p.calcular_indice(), reverse=True)

    def mostrar_fila(self, titulo, limite=10):
        self.repriorizar_fila()
        print(f"\n{titulo} (Mostrando top {limite})")
        print(f"{'Pos.':<5} {'Pedido':<10} {'Prior.':<8} {'Prazo':<8} {'Tam.':<5} {'Índice':<8} {'Situação'}")
        print("-" * 65)
        for i, p in enumerate(self.fila[:limite], 1):
            prazo_str = f"{p.prazo}m"
            print(f"{i:<5} {p.id_pedido:<10} {p.prioridade:<8} {prazo_str:<8} {p.tamanho:<5} {p.calcular_indice():<8.2f} {p.obter_situacao()}")
        print(f"... e mais {max(0, len(self.fila) - limite)} pedidos na fila.")
        print("-" * 65)

    def despachar_primeiro(self):
        if not self.fila:
            return
        
        self.repriorizar_fila()
        pedido = self.fila.pop(0)
        status_sla = "DENTRO DO PRAZO" if pedido.prazo >= 0 else "ATRASADO"
        
        self.historico_expedicao.append({
            "pedido": pedido.id_pedido,
            "minuto_despacho": self.tempo_simulado,
            "prazo_restante": pedido.prazo,
            "status_sla": status_sla
        })
        
        print(f"EXPEDINDO: {pedido.id_pedido} | Urgência: {pedido.calcular_indice():.2f} | Prazo restante: {pedido.prazo}m | {status_sla}")

    def avancar_tempo(self, minutos):
        print(f"\n=> Relógio avança {minutos} minutos. Tempo simulado atual: {self.tempo_simulado + minutos} minutos.")
        self.tempo_simulado += minutos
        for pedido in self.fila:
            pedido.prazo -= minutos

    def gerar_relatorio_metricas(self):
        print("\n" + "="*50)
        print("MÉTRICAS DA OPERAÇÃO (RELATÓRIO HOT)")
        print("="*50)
        
        total_despachados = len(self.historico_expedicao)
        if total_despachados == 0:
            print("Nenhum pedido foi despachado.")
            return

        no_prazo = sum(1 for h in self.historico_expedicao if h["status_sla"] == "DENTRO DO PRAZO")
        atrasados = total_despachados - no_prazo
        taxa_atraso = (atrasados / total_despachados) * 100
        
        minutos_atraso_total = sum(abs(h["prazo_restante"]) for h in self.historico_expedicao if h["prazo_restante"] < 0)
        atraso_medio = minutos_atraso_total / total_despachados if total_despachados > 0 else 0
        
        tempo_horas = max(self.tempo_simulado / 60, 0.1)
        throughput = total_despachados / tempo_horas

        print(f"Tempo total de operação: {self.tempo_simulado} minutos ({tempo_horas:.1f} horas)")
        print(f"Total de pedidos processados: {total_despachados}")
        print(f"✅ Pedidos entregues no prazo: {no_prazo}")
        print(f"❌ Pedidos atrasados (Estouro de SLA): {atrasados}")
        print(f"📉 Taxa de atraso (Furo de SLA): {taxa_atraso:.2f}%")
        print(f"⏱️ Atraso médio por pedido da operação: {atraso_medio:.1f} minutos")
        print(f"🚀 Throughput (Vazão): {throughput:.1f} pedidos/hora")

if __name__ == '__main__':
    simulador = SimuladorSLA()
    pedidos_iniciais = []

    tamanhos_disponiveis = ['P', 'M', 'G']
    for i in range(1, 41):
        id_ped = f"ORD-{i:03d}"
        prioridade_rand = random.randint(10, 100)
        prazo_rand = random.randint(15, 180) 
        tamanho_rand = random.choice(tamanhos_disponiveis)
        
        pedidos_iniciais.append(Pedido(id_ped, prioridade_rand, prazo_rand, tamanho_rand))

    simulador.carregar_pedidos(pedidos_iniciais)
    simulador.mostrar_fila("ETAPA 2 - ORDEM INICIAL DOS 40 PEDIDOS (PRÉ-OPERAÇÃO)")

    ciclo = 1
    while simulador.fila:
        print(f"\n--- CICLO DE EXPEDIÇÃO {ciclo} ---")
        
        qtd_a_despachar = random.randint(2, 5)
        for _ in range(qtd_a_despachar):
            if simulador.fila:
                simulador.despachar_primeiro()
        
        if simulador.fila:
            tempo_gasto = random.randint(10, 25)
            simulador.avancar_tempo(tempo_gasto)
            
        ciclo += 1

    simulador.gerar_relatorio_metricas()
