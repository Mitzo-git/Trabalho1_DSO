from datetime import date, datetime
from entidade.pessoa import Pessoa
from exceptions.dado_invalido_exception import DadoInvalidoException


class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_de_nascimento: date):
        super().__init__(nome, celular, cpf)
        self.__data_de_nascimento = data_de_nascimento

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: date):
        if not isinstance(data_de_nascimento, date) or isinstance(data_de_nascimento, datetime):
            raise DadoInvalidoException('Informe uma data de nascimento válida')
        if data_de_nascimento > date.today():
            raise DadoInvalidoException('A data de nascimento não pode estar no futuro')
        self.__data_de_nascimento = data_de_nascimento

    def calcula_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.__data_de_nascimento.year
        # ainda não fez aniversário este ano: tira 1
        if (hoje.month, hoje.day) < (self.__data_de_nascimento.month, self.__data_de_nascimento.day):
            idade -= 1
        return idade