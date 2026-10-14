from datetime import datetime
from entidade.paciente import Paciente
from entidade.procedimento import Procedimento
from entidade.profissional_da_saude import ProfissionalDaSaude
from entidade.tipo_atendimento import TipoAtendimento

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

    @property
    def tipo_de_atendimento(self):
        return self.__tipo_de_atendimento

    @tipo_de_atendimento.setter
    def tipo_de_atendimento(self, tipo_de_atendimento: TipoAtendimento):
        self.__tipo_de_atendimento = tipo_de_atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: ProfissionalDaSaude):
        self.__profissional = profissional

    @property
    def procedimentos(self):
        return list(self.__procedimentos)  # cópia: ninguém altera a lista por fora

    # composição: quem cria o Procedimento é o próprio Atendimento
    def adiciona_procedimento(self, descricao: str, custo: float,profissional: ProfissionalDaSaude) -> Procedimento:
        procedimento = Procedimento(descricao, custo, profissional)
        self.__procedimentos.append(procedimento)
        return procedimento

    def remove_procedimento(self, procedimento: Procedimento):
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)