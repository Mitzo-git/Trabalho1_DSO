class ClinicaNaoEncontradaException(Exception):
    def __init__(self):
        super().__init__("Clínica não encontrada")