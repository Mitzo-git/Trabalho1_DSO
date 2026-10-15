from entidade.pagamento_dinheiro import PagamentoDinheiro
from entidade.pagamento_pix import PagamentoPix
from entidade.pagamento_cartao import PagamentoCartao
from tela.tela_pagamento import TelaPagamento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.atendimento_nao_encontrado_exception import AtendimentoNaoEncontradoException
from exceptions.pagamento_nao_encontrado_exception import PagamentoNaoEncontradoException
from exceptions.pagamento_apos_atendimento_exception import PagamentoAposAtendimentoException
from exceptions.valor_excede_restante_exception import ValorExcedeRestanteException
from exceptions.atendimento_quitado_exception import AtendimentoQuitadoException
from exceptions.valor_total_menor_que_pago_exception import ValorTotalMenorQuePagoException

excecoes_pagamento = (
    DadoInvalidoException,
    AtendimentoNaoEncontradoException,
    PagamentoNaoEncontradoException,
    PagamentoAposAtendimentoException,
    ValorExcedeRestanteException,
    AtendimentoQuitadoException,
)


class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__pagamentos = []
        self.__tela = TelaPagamento()
        self.__controlador_sistema = controlador_sistema

    @property
    def pagamentos(self):
        return list(self.__pagamentos)

    def pega_pagamentos_do_atendimento(self, atendimento):
        return [p for p in self.__pagamentos if p.atendimento is atendimento]

    def valor_restante(self, atendimento, ignorar=None) -> float:
        pago = sum(p.valor_pago for p in self.__pagamentos
                   if p.atendimento is atendimento and p is not ignorar)
        return round(atendimento.calcular_valor_total() - pago, 2)

    def valida_novo_total(self, atendimento, novo_total: float):
        total_pago = sum(p.valor_pago for p in self.pega_pagamentos_do_atendimento(atendimento))
        if round(novo_total, 2) < round(total_pago, 2):
            raise ValorTotalMenorQuePagoException(total_pago)

    def __resumo(self, atendimento) -> dict:
        restante = self.valor_restante(atendimento)
        total = atendimento.calcular_valor_total()
        return {"valor_total": total,
                "valor_pago": round(total - restante, 2),
                "valor_restante": restante}

    def __valida_dados(self, dados: dict, atendimento, restante: float):
        if dados["valor_pago"] <= 0:
            raise DadoInvalidoException("O valor pago deve ser maior que zero")

        data_atendimento = atendimento.horario_inicio.date()
        if dados["data"] > data_atendimento:
            raise PagamentoAposAtendimentoException(data_atendimento)

        if round(dados["valor_pago"], 2) > restante:
            raise ValorExcedeRestanteException(restante)

        if dados["forma"] == "pix":
            cpf = dados["cpf_pagador"]
            if not cpf.isdigit() or len(cpf) != 11:
                raise DadoInvalidoException("CPF do pagador deve ter 11 dígitos numéricos")
        elif dados["forma"] == "cartao":
            numero = dados["numero_cartao"]
            if not numero.isdigit() or not 13 <= len(numero) <= 19:
                raise DadoInvalidoException("Número do cartão deve ter de 13 a 19 dígitos numéricos")
            if not dados["bandeira"].strip():
                raise DadoInvalidoException("A bandeira do cartão não pode ser vazia")

    def __cria_pagamento(self, dados: dict, atendimento):
        comuns = (dados["data"], atendimento.calcular_valor_total(), dados["valor_pago"],
                  atendimento, atendimento.paciente)
        if dados["forma"] == "pix":
            return PagamentoPix(dados["cpf_pagador"], *comuns)
        if dados["forma"] == "cartao":
            return PagamentoCartao(int(dados["numero_cartao"]), dados["bandeira"].strip(), *comuns)
        return PagamentoDinheiro(*comuns)

    def __seleciona_pagamento(self):
        if not self.__pagamentos:
            raise PagamentoNaoEncontradoException()
        self.listar()
        numero = self.__tela.seleciona()
        if not 1 <= numero <= len(self.__pagamentos):
            raise PagamentoNaoEncontradoException()
        return self.__pagamentos[numero - 1]

    def incluir(self):
        try:
            atendimento = self.__controlador_sistema.controlador_atendimento.seleciona_atendimento()
            restante = self.valor_restante(atendimento)
            if restante <= 0:
                raise AtendimentoQuitadoException()

            self.__tela.mostra_resumo(self.__resumo(atendimento))
            dados = self.__tela.pega_dados()
            self.__valida_dados(dados, atendimento, restante)

            self.__pagamentos.append(self.__cria_pagamento(dados, atendimento))
            self.__tela.mostra_mensagem("Pagamento registrado com sucesso")
            self.__tela.mostra_resumo(self.__resumo(atendimento))
        except excecoes_pagamento as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            pagamento = self.__seleciona_pagamento()
            atendimento = pagamento.atendimento
            restante = self.valor_restante(atendimento, ignorar=pagamento)

            dados = self.__tela.pega_dados()
            self.__valida_dados(dados, atendimento, restante)

            posicao = self.__pagamentos.index(pagamento)
            self.__pagamentos[posicao] = self.__cria_pagamento(dados, atendimento)
            self.__tela.mostra_mensagem("Pagamento alterado com sucesso")
        except excecoes_pagamento as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            pagamento = self.__seleciona_pagamento()
            self.__pagamentos.remove(pagamento)
            self.__tela.mostra_mensagem("Pagamento excluído com sucesso")
        except excecoes_pagamento as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__pagamentos:
            self.__tela.mostra_mensagem("Nenhum pagamento registrado")
            return
        for numero, p in enumerate(self.__pagamentos, start=1):
            self.__tela.mostra_dados({
                "numero": numero,
                "data": p.data,
                "forma": p.forma,
                "paciente": p.paciente.nome,
                "horario_atendimento": p.atendimento.horario_inicio,
                "valor_pago": p.valor_pago,
                "valor_restante": self.valor_restante(p.atendimento),
            })

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()