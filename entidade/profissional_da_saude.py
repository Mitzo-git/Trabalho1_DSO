from entidade.pessoa import Pessoa
from exceptions.dado_invalido_exception import DadoInvalidoException


class ProfissionalDaSaude(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, especialidade: str, registro: str):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str):
        if not isinstance(especialidade, str) or not especialidade.strip():
            raise DadoInvalidoException('A especialidade não pode ser vazia')
        self.__especialidade = especialidade.strip()

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro: str):
        if not isinstance(registro, str) or not registro.strip():
            raise DadoInvalidoException('O registro profissional não pode ser vazio')
        self.__registro = registro.strip()