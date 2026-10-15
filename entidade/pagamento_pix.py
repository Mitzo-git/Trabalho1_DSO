from datetime import date
from entidade.pagamento import Pagamento
from entidade.atendimento import Atendimento
from entidade.paciente import Paciente

class PagamentoPix(Pagamento):
    def __init__(self, cpf_pagador: str, data: date, valor_total: float, valor_pago: float, atendimento: Atendimento, paciente: Paciente):
        super().__init__(data, valor_total, valor_pago, atendimento, paciente)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador

    @property
    def forma(self):
        return "PIX"