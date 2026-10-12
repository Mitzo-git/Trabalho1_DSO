from datetime import
from entidade.paciente import Paciente
from entidade.profissional_da_saude import ProfissionalDaSaude
from entidade.tipo_atendimento import TipoAtendimento

class Atendimento:
    def __init__(self, horario_inicio: time, horario_fim: time, valor: float, tipo_de_atendimento: TipoAtendimento,  paciente: Paciente, profissional: ProfissionalDaSaude):
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__tipo_de_atendimento = tipo_de_atendimento
        self.__paciente = paciente
        self.__profissional = profissional
        self.__procedimentos= []