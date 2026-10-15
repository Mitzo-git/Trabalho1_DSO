from entidade.pagamento import Pagamento
from datetime import date
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao: int, bandeira: str, data: date, valor_total: float, valor_pago: float, atendimento: Atendimento, paciente: Paciente):
        super().__init__(data, valor_total, valor_pago, atendimento, paciente)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: int):
        if not isinstance(numero_cartao, int):
            raise TypeError("O número do cartão deve ser um número inteiro válido.")
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira

    @property
    def forma(self):
        return "Cartão de crédito"