class ProfissionalNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Profissional não encontrado")