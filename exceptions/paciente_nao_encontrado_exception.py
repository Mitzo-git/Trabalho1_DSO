class PacienteNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Paciente não encontrado")