class DadoInvalidoException(Exception):
    def __init__(self, mensagem="Dado inválido"):
        super().__init__(mensagem)