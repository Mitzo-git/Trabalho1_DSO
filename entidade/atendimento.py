import datetime from datetime

class Atendimento:
    def __init__(self, horario_inicio: datetime, horario_fim: datetime, valor: float, tipo_de_atendimento: TipoAtendimento,  paciente: Paciente, profissional: ProfissionalDaSaude):
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__tipo_de_atendimento = tipo_de_atendimento
        self.__paciente = paciente
        self.__profissional = profissional
        self.__procedimentos= [] #composição

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: datetime):
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: datetime):
        self.__horario_fim = horario_fim

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor
