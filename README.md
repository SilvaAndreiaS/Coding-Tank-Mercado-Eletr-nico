## Fluxograma do Sistema (MPS)

```mermaid
flowchart TD
    A(["INÍCIO — VelozMart S.A."]) --> B["Receber pedidos do marketplace"]

    B --> C["Ler dados do pedido<br/>ID, prioridade IA, prazo, tamanho e região"]
    C --> D{"Todos os dados são válidos?"}

    D -- "Não" --> E["Registrar erro de validação"]
    E --> F["Solicitar correção dos dados"]
    F --> B

    D -- "Sim" --> G["Registrar horário de entrada"]
    G --> H["Calcular prioridade do pedido"]

    H --> H1["Normalizar pontuação de IA"]
    H1 --> H2["Calcular urgência conforme prazo restante"]
    H2 --> H3["Considerar tamanho e eficiência operacional"]
    H3 --> H4["Aplicar regra de desempate por tempo de espera"]

    H4 --> I["Inserir pedido na fila de prioridade heapq"]
    I --> J["Atualizar painel de pedidos e indicadores"]

    J --> K{"Existem pedidos aguardando?"}
    K -- "Não" --> L["Aguardar novos pedidos ou atualizações"]
    L --> B

    K -- "Sim" --> M["Verificar prazos e prioridades atualizadas"]
    M --> N["Selecionar pedido de maior prioridade"]

    N --> O{"Pedido está apto para despacho?"}
    O -- "Não" --> P["Registrar impedimento e motivo"]
    P --> P1["Reavaliar prioridade e disponibilidade"]
    P1 --> K

    O -- "Sim" --> Q["Retirar pedido da fila"]
    Q --> R["Encaminhar para doca de expedição"]
    R --> S["Registrar início e conclusão da expedição"]

    S --> T["Atualizar status do pedido"]
    T --> U["Calcular tempo de espera e situação do SLA"]
    U --> V["Atualizar métricas logísticas e financeiras"]

    V --> W["Consolidar indicadores por região"]
    W --> X{"Há outros pedidos aguardando?"}

    X -- "Sim" --> M
    X -- "Não" --> Y["Gerar relatório operacional"]

    Y --> Z["Comparar desempenho com FIFO"]
    Z --> AA["Avaliar atrasos, tempo de espera e produtividade"]
    AA --> AB(["FIM DO CICLO — Monitorar e reiniciar"])

    AB --> B


```
