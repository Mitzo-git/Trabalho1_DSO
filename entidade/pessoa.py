from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, celular: str, cpf: str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular: str):
        self.__celular = celular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf= cpf
