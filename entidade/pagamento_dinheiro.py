from datetime import date
from entidade.pagamento import Pagamento
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, valor_total: float, valor_pago: float, atendimento: Atendimento, paciente: Paciente):
        super().__init__(data, valor_total, valor_pago, atendimento, paciente)