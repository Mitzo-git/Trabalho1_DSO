from datetime import datetime

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str, horario_abertura: time, horario_fechamento: datetime):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        #self.__valida_horarios(horario_abertura, horario_fechamento)
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__atendimentos= []  #agregação: a clínica reúne seus atendimentos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time):
        #self.__valida_horarios(horario_abertura, self.__horario_fechamento) validação de horario
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time):
        #self.__valida_horarios(horario_abertura, self.__horario_fechamento)
        self.__horario_fechamento = horario_fechamento

    @property
    def atendimentos(self):
        return self.__atendimentos #cópia que evita que alguem altere a lista por fora

    #métodos com o atendimento