class ValorExcedeRestanteException(Exception):
    def __init__(self, restante: float):
        super().__init__(f"O valor pago excede o valor restante do atendimento (R$ {restante:.2f})")