from abc import ABC, abstractmethod
from exceptions.dado_invalido_exception import DadoInvalidoException


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
        if not isinstance(nome, str) or not nome.strip():
            raise DadoInvalidoException('O nome não pode ser vazio')
        self.__nome = nome.strip()

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular: str):
        if not isinstance(celular, str):
            raise DadoInvalidoException('O celular deve ser um texto')
        # aceita "(48) 99999-9999" e guarda só os números
        numeros = ''.join(c for c in celular if c.isdigit())
        if len(numeros) not in (10, 11):
            raise DadoInvalidoException('O celular deve ter 10 ou 11 números (com DDD)')
        self.__celular = numeros

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if not isinstance(cpf, str):
            raise DadoInvalidoException('O CPF deve ser um texto')
        numeros = cpf.replace('.', '').replace('-', '').strip()
        if len(numeros) != 11 or not numeros.isdigit():
            raise DadoInvalidoException('O CPF deve ter 11 números')
        self.__cpf = numeros
