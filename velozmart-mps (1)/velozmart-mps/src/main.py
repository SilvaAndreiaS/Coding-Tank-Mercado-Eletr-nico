from pathlib import Path
from .logistica import carregar_pedidos
from .relatorios import exportar_fila_csv

DADOS = [
    ("ORD-001", 90, 120, "P"),
    ("ORD-002", 60, 15, "M"),
    ("ORD-003", 40, 180, "G"),
    ("ORD-004", 85, 30, "P"),
    ("ORD-005", 70, 45, "M"),
    ("ORD-006", 95, 240, "G"),
    ("ORD-007", 55, 10, "P"),
    ("ORD-008", 80, 60, "M"),
    ("ORD-009", 30, 5, "G"),
    ("ORD-010", 75, 90, "P"),
    ("ORD-011", 65, 20, "G"),
    ("ORD-012", 50, 75, "M"),
]


def main():
    sistema = carregar_pedidos(DADOS)
    sistema.mostrar_fila("ETAPA 1 — CLASSIFICAÇÃO INICIAL")
    sistema.explicar_ordem()

    print("\nETAPA 2 — PRIMEIRO DESPACHO")
    sistema.despachar()

    sistema.atualizar_tempo(12)
    sistema.mostrar_fila("ETAPA 3 — FILA APÓS 12 MINUTOS")

    print("\nETAPA 4 — SEGUNDO DESPACHO")
    sistema.despachar()
    sistema.mostrar_fila("ETAPA 5 — PEDIDOS AINDA AGUARDANDO")

    caminho = Path(__file__).resolve().parent.parent / "reports" / "fila_prioridade.csv"
    exportar_fila_csv(sistema.listar_ordenados(), str(caminho))
    print(f"\nRelatório CSV salvo em: {caminho}")


if __name__ == "__main__":
    main()
