from entidade.profissional_da_saude import ProfissionalDaSaude
from exceptions.dado_invalido_exception import DadoInvalidoException


class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: ProfissionalDaSaude):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if not isinstance(descricao, str) or not descricao.strip():
            raise DadoInvalidoException('A descrição do procedimento não pode ser vazia')
        self.__descricao = descricao.strip()

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if isinstance(custo, bool) or not isinstance(custo, (int, float)) or custo <= 0:
            raise DadoInvalidoException('O custo deve ser um número maior que zero')
        self.__custo = custo

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: ProfissionalDaSaude):
        if not isinstance(profissional, ProfissionalDaSaude):
            raise DadoInvalidoException('Profissional inválido')
        self.__profissional = profissional