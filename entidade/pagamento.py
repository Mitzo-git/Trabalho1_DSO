from abc import ABC, abstractmethod
from datetime import date
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente

class Pagamento(ABC):
    def __init__(self, data: date, valor_total: float, valor_pago: float, atendimento: Atendimento, paciente: Paciente):
        self.__data = date
        self.__valor_total = valor_total
        self.__valor_pago = valor_pago
        self.__atendimento = atendimento
        self.__paciente = paciente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__date = data

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total: float):
        self.__valor_total = valor_total

    #calculo valor restante
    @property
    def valor_restante(self):
        return self.__valor_total - self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        self.__atendimento = atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

