class TipoAtendimentoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Tipo de atendimento não encontrado")