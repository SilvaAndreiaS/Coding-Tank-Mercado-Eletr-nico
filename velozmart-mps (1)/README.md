# VelozMart MPS — Marketplace Priority Sorter

Protótipo em Python para organizar pedidos de expedição por urgência, prazo e ordem de chegada.

## Requisitos
- Python 3.10 ou superior
- Não utiliza dependências externas para executar o protótipo.

## Como executar
Na pasta do projeto:

```bash
python -m src.main
```

## Como executar os testes
```bash
python -m unittest discover -s tests -v
```

## Critérios de ordenação
1. Pedidos com prazo vencido (prazo <= 0) primeiro.
2. Maior urgência: `prioridade * peso_tamanho / max(prazo, 1)`.
3. Menor prazo restante.
4. Ordem de entrada, em caso de empate.

Pesos de tamanho: P = 1.0, M = 1.2, G = 1.5.

> Observação: o prazo é atualizado em minutos. Um pedido pode ficar com prazo negativo após a passagem do tempo; isso representa atraso.
