from datetime import date
from entidade.pagamento import Pagamento
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente
from exceptions.dado_invalido_exception import DadoInvalidoException


class PagamentoPix(Pagamento):
    def __init__(self, cpf_pagador: str, data: date, valor_total: float, valor_pago: float,
                 atendimento: Atendimento, paciente: Paciente):
        super().__init__(data, valor_total, valor_pago, atendimento, paciente)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        if not isinstance(cpf_pagador, str):
            raise DadoInvalidoException('O CPF deve ser um texto')
        # tira pontos e traço, então "123.456.789-09" também é aceito
        numeros = cpf_pagador.replace('.', '').replace('-', '').strip()
        if len(numeros) != 11 or not numeros.isdigit():
            raise DadoInvalidoException('O CPF deve ter 11 números')
        self.__cpf_pagador = numeros