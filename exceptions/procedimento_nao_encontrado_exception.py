class ProcedimentoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Procedimento não encontrado")