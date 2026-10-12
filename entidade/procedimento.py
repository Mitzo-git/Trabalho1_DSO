from entidade.profissional_da_saude import ProfissionalDaSaude

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: ProfissionalDaSaude):
        self.__descricao= descricao
        self.__custo= custo
        self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao #texto nao vazio tratar exceção

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo: float): #valor pode ser invalido: negativo, igual a zero etc tratar nas exceções
        self.__custo = custo

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: ProfissionalDaSaude):
        return self.__profissional = profissional