from datetime import datetime
from entidade.tipo_atendimento import TipoAtendimento
from entidade.paciente import Paciente
from entidade.profissional_da_saude import ProfissionalDaSaude
from entidade.procedimento import Procedimento
from entidade.clinica import Clinica
from exceptions.dado_invalido_exception import DadoInvalidoException


class Atendimento:
    def __init__(self, horario_inicio: datetime, horario_fim: datetime, valor: float,tipo_de_atendimento: TipoAtendimento, paciente: Paciente,profissional: ProfissionalDaSaude, clinica: Clinica):

        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__tipo_de_atendimento = tipo_de_atendimento
        self.__paciente = paciente
        self.__profissional = profissional
        self.__clinica = clinica
        self.__procedimentos = []  #composição: o atendimento cria seus procedimentos

    # ---------- horários ----------
    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    def altera_horarios(self, inicio: datetime, fim: datetime):
        self.__valida_horarios(inicio, fim)
        self.__horario_inicio = inicio
        self.__horario_fim = fim

    # ---------- valor ----------
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor < 0:
            raise DadoInvalidoException('O valor deve ser um número maior ou igual a zero')
        self.__valor = valor

    # ---------- tipo de atendimento ----------
    @property
    def tipo_de_atendimento(self):
        return self.__tipo_de_atendimento

    @tipo_de_atendimento.setter
    def tipo_de_atendimento(self, tipo_de_atendimento: TipoAtendimento):
        if not isinstance(tipo_de_atendimento, TipoAtendimento):
            raise DadoInvalidoException('Tipo de atendimento inválido')
        self.__tipo_de_atendimento = tipo_de_atendimento

    # ---------- paciente ----------
    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise DadoInvalidoException('Paciente inválido')
        self.__paciente = paciente

    # ---------- profissional ----------
    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: ProfissionalDaSaude):
        if not isinstance(profissional, ProfissionalDaSaude):
            raise DadoInvalidoException('Profissional inválido')
        self.__profissional = profissional

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        if not isinstance(clinica, Clinica):
            raise DadoInvalidoException('Clinica inválida')
        self.__clinica = clinica

    # ---------- procedimentos (composição) ----------
    @property
    def procedimentos(self):
        return list(self.__procedimentos)  # cópia: ninguém altera a lista por fora

    def adiciona_procedimento(self, descricao: str, custo: float,
                              profissional: ProfissionalDaSaude) -> Procedimento:
        # quem cria o Procedimento é o próprio Atendimento
        procedimento = Procedimento(descricao, custo, profissional)
        self.__procedimentos.append(procedimento)
        return procedimento

    def remove_procedimento(self, procedimento: Procedimento):
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)

    # valor total do atendimento: valor base + custo de cada procedimento
    def valor_total(self) -> float:
        return self.__valor + sum(p.custo for p in self.__procedimentos)

    # ---------- validação privada ----------
    @staticmethod
    def __valida_horarios(inicio, fim):
        if not isinstance(inicio, datetime) or not isinstance(fim, datetime):
            raise DadoInvalidoException('Os horários devem ser data e hora')
        if inicio >= fim:
            raise DadoInvalidoException('O início deve ser antes do fim do atendimento')
        if inicio.date() != fim.date():
            raise DadoInvalidoException('O atendimento deve começar e terminar no mesmo dia')
