from abc import ABC, abstractmethod
from datetime import date, datetime
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente
from exceptions.dado_invalido_exception import DadoInvalidoException


class Pagamento(ABC):
    @abstractmethod  # impede criar Pagamento() direto; só as filhas (cartão, pix etc.) são criadas
    def __init__(self, data: date, valor_total: float, valor_pago: float,
                 atendimento: Atendimento, paciente: Paciente):
        self.__data = data
        self.__valor_total = valor_total
        self.__valor_pago = valor_pago
        self.__atendimento = atendimento
        self.__paciente = paciente

    # ---------- data ----------
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if not isinstance(data, date) or isinstance(data, datetime):
            raise DadoInvalidoException('A data do pagamento é inválida')
        self.__data = data

    # ---------- valores ----------
    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total: float):
        self.__valida_valores(valor_total, self.__valor_pago)
        self.__valor_total = valor_total

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valida_valores(self.__valor_total, valor_pago)
        self.__valor_pago = valor_pago

    # cálculo do valor restante (não tem setter: é sempre calculado)
    @property
    def valor_restante(self):
        return self.__valor_total - self.__valor_pago

    # ---------- atendimento ----------
    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        if not isinstance(atendimento, Atendimento):
            raise DadoInvalidoException('Atendimento inválido')
        self.__atendimento = atendimento

    # ---------- paciente ----------
    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise DadoInvalidoException('Paciente inválido')
        self.__paciente = paciente

    # ---------- validação privada ----------
    @staticmethod
    def __valida_valores(total, pago):
        for valor in (total, pago):
            if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0:
                raise DadoInvalidoException('Os valores devem ser números maiores ou iguais a zero')
        if pago > total:
            raise DadoInvalidoException('O valor pago não pode ser maior que o valor total')

    @abstractmethod
    def forma(self):
        pass
