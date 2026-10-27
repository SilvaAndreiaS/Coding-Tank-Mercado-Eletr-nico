#  Marketplace Priority Sorter (MPS) — VelozMart

> Solução conceitual e algorítmica para ordenação inteligente e dinâmica de pedidos de expedição em tempo real. Projeto desenvolvido para o Coding Tank de **Ordenação e Prioridade**.

---

##  1. Problema

O **VelozMart** lida com um volume dinâmico de pedidos aguardando despacho em docas de embalagem com espaço e tempo limitados. Uma ordenação ingênua (como FIFO/ordem de chegada) gera multas de SLA, gargalos nas docas com pacotes volumosos e negligência de pedidos de alto valor. O desafio consiste em ordenar e reordenar continuamente os pedidos com base em múltiplos critérios conflitantes, minimizando atrasos e custos operacionais.

* **Dados de entrada de cada pedido:**
  * `priorityScore` ($0$ a $100$): calculado por IA (distância, valor, reputação, cliente).
  * `dispatchWindow` (minutos restantes): tempo limite antes da quebra de SLA.
  * `sizeCategory` (`P`, `M`, `G`): impacto físico no buffer da doca.

---

##  2. Algoritmo e Estrutura de Dados

### 2.1 Estrutura Escolhida: **Max-Heap Dinâmico (Fila de Prioridade)**
Para balancear alto throughput com inserções e atualizações contínuas, a solução adota um **Max-Heap** indexado por uma tabela hash (para buscas e atualizações em $O(\log n)$ por ID de pedido).

### 2.2 Função de Pontuação Composta ($K_{score}$)
A chave de prioridade de cada pedido é calculada em tempo real pela fórmula:

$$K_{score} = \left( \text{priorityScore} \times W_{score} + \frac{C_{urgencia}}{\max(\text{dispatchWindow}, 1)} \right) \times M_{tamanho}$$

* **Janela Crítica (SLA):** Conforme `dispatchWindow` aproxima-se de zero, o divisor reduz drasticamente, elevando a chave ao topo da fila.
* **Penalidade de Doca ($M_{tamanho}$):** Pedidos `P` e `M` recebem leve bônus de vazão ($1.05$ e $1.00$), enquanto `G` ($0.90$) é despachado prioritariamente quando as docas dedicadas a grandes volumes estiverem liberadas.

---

### 2.3 Pseudocódigo Operacional

```python
classe Pedido:
    id: string
    priorityScore: float      # 0 a 100
    dispatchWindow: int       # Minutos restantes
    sizeCategory: string      # 'P', 'M', 'G'

funcao calcular_chave(pedido):
    fator_urgencia = 1.0 / max(pedido.dispatchWindow, 1)
    modificador_tamanho = {'P': 1.05, 'M': 1.00, 'G': 0.90}[pedido.sizeCategory]
    
    # Se prazo estiver vencido ou crítico (< 15 min), prioridade máxima
    se pedido.dispatchWindow <= 15:
        retornar (10000 - pedido.dispatchWindow) + pedido.priorityScore
    
    retornar (pedido.priorityScore * 0.6 + fator_urgencia * 400) * modificador_tamanho

classe MarketplacePrioritySorter:
    heap = MaxHeap()
    mapa_pedidos = Dicionario()

    funcao inserir_ou_atualizar(pedido):
        chave = calcular_chave(pedido)
        se pedido.id em mapa_pedidos:
            heap.atualizar_chave(pedido.id, chave)
        senao:
            heap.inserir(pedido, chave)
            mapa_pedidos[pedido.id] = pedido

    funcao proximo_para_despacho(doca_disponivel, tamanho_doca):
        # Remove o topo com maior prioridade compatível com a doca
        pedido = heap.extrair_maximo_compativel(tamanho_doca)
        remover mapa_pedidos[pedido.id]
        retornar pedido`

```

classe Pedido:
    id: string
    priorityScore: float      # 0 a 100
    dispatchWindow: int       # Minutos restantes
    sizeCategory: string      # 'P', 'M', 'G'

funcao calcular_chave(pedido):
    fator_urgencia = 1.0 / max(pedido.dispatchWindow, 1)
    modificador_tamanho = { 'P': 1.05, 'M': 1.0, 'G': 0.90 }[pedido.sizeCategory]
    
    # Se prazo estiver vencido ou crítico (< 15 min), prioridade máxima
    se pedido.dispatchWindow <= 15:
        retornar (10000 - pedido.dispatchWindow) + pedido.priorityScore
    
    retornar (pedido.priorityScore * 0.6 + fator_urgencia * 400) * modificador_tamanho

classe MarketplacePrioritySorter:
    heap = MaxHeap()
    mapa_pedidos = Dicionario()

    funcao inserir_ou_atualizar(pedido):
        chave = calcular_chave(pedido)
        se pedido.id em mapa_pedidos:
            heap.atualizar_chave(pedido.id, chave)
        senao:
            heap.inserir(pedido, chave)
            mapa_pedidos[pedido.id] = pedido

    funcao proximo_para_despacho(doca_disponivel, tamanho_doca):
        # Remove o topo com maior prioridade compatível com a doca
        pedido = heap.extrair_maximo_compativel(tamanho_doca)
        remover mapa_pedidos[pedido.id]
        retornar pedido


classe Pedido:
    id: string
    priorityScore: float      # 0 a 100
    dispatchWindow: int       # Minutos restantes
    sizeCategory: string      # 'P', 'M', 'G'

funcao calcular_chave(pedido):
    fator_urgencia = 1.0 / max(pedido.dispatchWindow, 1)
    modificador_tamanho = { 'P': 1.05, 'M': 1.0, 'G': 0.90 }[pedido.sizeCategory]
    
    # Se prazo estiver vencido ou crítico (< 15 min), prioridade máxima
    se pedido.dispatchWindow <= 15:
        retornar (10000 - pedido.dispatchWindow) + pedido.priorityScore
    
    retornar (pedido.priorityScore * 0.6 + fator_urgencia * 400) * modificador_tamanho

classe MarketplacePrioritySorter:
    heap = MaxHeap()
    mapa_pedidos = Dicionario()

    funcao inserir_ou_atualizar(pedido):
        chave = calcular_chave(pedido)
        se pedido.id em mapa_pedidos:
            heap.atualizar_chave(pedido.id, chave)
        senao:
            heap.inserir(pedido, chave)
            mapa_pedidos[pedido.id] = pedido

    funcao proximo_para_despacho(doca_disponivel, tamanho_doca):
        # Remove o topo com maior prioridade compatível com a doca
        pedido = heap.extrair_maximo_compativel(tamanho_doca)
        remover mapa_pedidos[pedido.id]
        retornar pedido


```


