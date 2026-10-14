class ProfissionalJaCadastradoException(Exception):
    def __init__(self):
        super().__init__("Já existe um profissional cadastrado com esse CPF")