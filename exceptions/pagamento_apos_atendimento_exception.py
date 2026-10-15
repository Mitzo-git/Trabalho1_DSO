from datetime import date

class PagamentoAposAtendimentoException(Exception):
    def __init__(self, data_limite: date):
        super().__init__("O pagamento deve ser realizado até a data do atendimento "
                         f"({data_limite.strftime('%d/%m/%Y')})")