class AtendimentoComPagamentoException(Exception):
    def __init__(self):
        super().__init__("O atendimento possui pagamentos registrados e não pode ser excluído")