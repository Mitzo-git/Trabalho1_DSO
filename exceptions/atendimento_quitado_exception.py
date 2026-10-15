class AtendimentoQuitadoException(Exception):
    def __init__(self):
        super().__init__("Este atendimento já está totalmente pago")