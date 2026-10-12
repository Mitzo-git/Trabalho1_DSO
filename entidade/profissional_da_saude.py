from entidade.pessoa import Pessoa

class ProfissionalDaSaude(Pessoa):
    def __init__(self, nome:str, celular:str, cpf: str, especialidade: str, registro: str ):
        super().__init__(nome, celular, cpf)
        self.__especialidade= especialidade
        self.__registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade:str):
        self.__especialidade= especialidade

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro: str):
        self.__registro = registro
