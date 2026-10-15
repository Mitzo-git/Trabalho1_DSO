class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao: str, bandeira: str, data: date, valor_total: float, valor_pago: float, atendimento: Atendimento, paciente: Paciente):

        super().__init__(data, valor_total, valor_pago, atendimento, paciente)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        if not isinstance(numero_cartao, str) or len(numero_cartao.strip()) == 0:
            raise DadoInvalidoException("numero_cartao", "O número do cartão deve ser um texto válido.")
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str):
        if not isinstance(bandeira, str) or len(bandeira.strip()) == 0:
            raise DadoInvalidoException("bandeira", "A bandeira não pode estar vazia.")
        self.__bandeira = bandeira