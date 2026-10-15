from exceptions.dado_invalido_exception import DadoInvalidoException

class TipoAtendimento:
    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise DadoInvalidoException('O nome do tipo de atendimento não pode ser vazio')
        self.__nome = nome.strip()