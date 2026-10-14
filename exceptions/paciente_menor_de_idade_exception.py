class PacienteMenorDeIdadeException(Exception):
    def __init__(self):
        super().__init__("Paciente menor de idade: não pode realizar atendimento de forma independente")