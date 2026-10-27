import csv
import os


def exportar_fila_csv(pedidos, caminho):
    """Exporta a fila ordenada para CSV."""
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["id_pedido", "prioridade", "prazo_minutos",
                  "tamanho", "urgencia", "situacao"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for pedido in pedidos:
            if pedido.prazo <= 0:
                situacao = "ATRASADO"
            elif pedido.prazo <= 15:
                situacao = "CRITICO"
            elif pedido.prazo <= 60:
                situacao = "ATENCAO"
            else:
                situacao = "NO_PRAZO"
            escritor.writerow({
                "id_pedido": pedido.id_pedido,
                "prioridade": pedido.prioridade,
                "prazo_minutos": pedido.prazo,
                "tamanho": pedido.tamanho,
                "urgencia": round(pedido.urgencia, 4),
                "situacao": situacao,
            })
    return caminho
