class ClinicaJaCadastradaException(Exception):
    def __init__(self):
        super().__init__("Já existe uma clínica cadastrada com esse nome")