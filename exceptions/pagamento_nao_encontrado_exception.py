class PagamentoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Pagamento não encontrado")