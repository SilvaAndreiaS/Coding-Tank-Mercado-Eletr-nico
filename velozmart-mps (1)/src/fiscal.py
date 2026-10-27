"""Validações fiscais simples para o protótipo."""


def validar_identificador_pedido(id_pedido):
    if not isinstance(id_pedido, str) or not id_pedido.strip():
        raise ValueError("Identificador fiscal/pedido inválido.")
    return True


def validar_valor(valor):
    if not isinstance(valor, (int, float)) or valor < 0:
        raise ValueError("O valor deve ser numérico e não negativo.")
    return True
