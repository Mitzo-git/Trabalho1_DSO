class ValorTotalMenorQuePagoException(Exception):
    def __init__(self, total_pago: float):
        super().__init__("A alteração deixaria o valor total do atendimento menor que o já pago "
                         f"(R$ {total_pago:.2f})")