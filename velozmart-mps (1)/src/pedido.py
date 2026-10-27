class Pedido:
    """Representa um pedido que aguarda expedição."""

    PESOS_TAMANHO = {"P": 1.0, "M": 1.2, "G": 1.5}

    def __init__(self, id_pedido, prioridade, prazo, tamanho):
        if not 0 <= prioridade <= 100:
            raise ValueError("Prioridade deve estar entre 0 e 100.")
        if prazo < 0:
            # Prazos negativos podem surgir depois de atualizar o tempo,
            # mas um pedido novo deve começar com prazo não negativo.
            raise ValueError("O prazo inicial não pode ser negativo.")
        if tamanho not in self.PESOS_TAMANHO:
            raise ValueError("Tamanho deve ser P, M ou G.")
        if not id_pedido:
            raise ValueError("O identificador do pedido é obrigatório.")

        self.id_pedido = str(id_pedido)
        self.prioridade = float(prioridade)
        self.prazo = float(prazo)
        self.tamanho = tamanho
        self.urgencia = 0.0

    def calcular_urgencia(self):
        """Quanto maior o resultado, maior a prioridade calculada."""
        peso = self.PESOS_TAMANHO[self.tamanho]
        self.urgencia = self.prioridade * peso / max(self.prazo, 1)
        return self.urgencia
