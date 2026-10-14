class PacienteJaCadastradoException(Exception):
    def __init__(self):
        super().__init__("Já existe um paciente cadastrado com esse CPF")