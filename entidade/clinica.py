from exceptions.dado_invalido_exception import DadoInvalidoException
from datetime import time

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str, horario_abertura: time, horario_fechamento: time):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__atendimentos= []  #agregação: a clínica reúne seus atendimentos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = self.__valida_texto(nome, 'nome')

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = self.__valida_texto(cidade, 'cidade')

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = self.__valida_texto(descricao, 'descricao')

#---------------- acabou os do tipo str e nao ser vazio, agora é do tipo time e abertura antes do fechamento

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

#validar o par na ideia de "tudo ou nada", exemplificando: se o horário de abertura for igual ou maior que o horário de fechamento, de um erro avisando que é impossível
    def altera_horarios(self, abertura: time, fechamento: time):
        self.__valida_horarios(abertura, fechamento)
        self.__horario_abertura = abertura
        self.__horario_fechamento = fechamento

#-----agregação com e seus metodos-------------------

    @property
    def atendimentos(self):
        return self.__atendimentos #cópia que evita que alguem altere a lista por fora

    def adiciona_atendimento(self, atendimento):
        if atendimento in self.__atendimentos:
            self.__atendimentos.append(atendimento)

    def remove_atendimentos(self, atendimentos):
        if atendimentos in self.__atendimentos:
            self.__atendimentos.remove(atendimentos)

    #esse atendimento está dentro do expediente da clinica?
    def funciona_em(self, inicio: time, fim : time) -> bool:
        return self.__horario_abertura <= inicio < fim <= self.__horario_fechamento

    #metodos de validação privados

    @staticmethod
    def __valida_texto(valor, campo: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise DadoInvalidoException(f'O campo {campo} não pode ser vazio')
        return valor.strip()

    @staticmethod
    def __valida_horarios(abertura, fechamento):
        if not isinstance(abertura, time) or not isinstance(fechamento, time):
            raise DadoInvalidoException ('Os Horários devem ser do tipo hora')
        if abertura >= fechamento:
            raise DadoInvalidoException ('O Horário de abertura deve ser antes do fechamento')