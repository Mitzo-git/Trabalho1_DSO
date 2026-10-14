class AtendimentoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Atendimento não encontrado")