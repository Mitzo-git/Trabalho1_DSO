from tela.tela_procedimento import TelaProcedimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.atendimento_nao_encontrado_exception import AtendimentoNaoEncontradoException
from exceptions.profissional_nao_encontrado_exception import ProfissionalNaoEncontradoException
from exceptions.procedimento_nao_encontrado_exception import ProcedimentoNaoEncontradoException
from exceptions.valor_total_menor_que_pago_exception import ValorTotalMenorQuePagoException

excecoes_procedimento = (
    DadoInvalidoException,
    AtendimentoNaoEncontradoException,
    ProfissionalNaoEncontradoException,
    ProcedimentoNaoEncontradoException,
    ValorTotalMenorQuePagoException,
)


class ControladorProcedimento:
    def __init__(self, controlador_sistema):
        self.__tela = TelaProcedimento()
        self.__controlador_sistema = controlador_sistema

    def todos_procedimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        return [proc for atendimento in atendimentos for proc in atendimento.procedimentos]

    def __valida_dados(self, dados: dict):
        if not dados["descricao"].strip():
            raise DadoInvalidoException("A descrição não pode ser vazia")
        if dados["custo"] <= 0:
            raise DadoInvalidoException("O custo deve ser maior que zero")

    def __busca_profissional(self, cpf: str):
        profissional = self.__controlador_sistema.controlador_profissional.pega_profissional_por_cpf(cpf)
        if profissional is None:
            raise ProfissionalNaoEncontradoException()
        return profissional

    def __numero_do_atendimento(self, atendimento) -> int:
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        return atendimentos.index(atendimento) + 1

    def __mostra_do_atendimento(self, atendimento):
        numero_atendimento = self.__numero_do_atendimento(atendimento)
        for numero, proc in enumerate(atendimento.procedimentos, start=1):
            self.__tela.mostra_dados({
                "numero_atendimento": numero_atendimento,
                "paciente": atendimento.paciente.nome,
                "horario_atendimento": atendimento.horario_inicio,
                "numero": numero,
                "descricao": proc.descricao,
                "custo": proc.custo,
                "profissional": proc.profissional.nome,
            })

    def __seleciona_procedimento(self, atendimento):
        procedimentos = atendimento.procedimentos
        if not procedimentos:
            raise ProcedimentoNaoEncontradoException()
        self.__mostra_do_atendimento(atendimento)
        numero = self.__tela.seleciona()
        if not 1 <= numero <= len(procedimentos):
            raise ProcedimentoNaoEncontradoException()
        return procedimentos[numero - 1]

    def __seleciona_atendimento_e_incluir(self):
        try:
            atendimento = self.__controlador_sistema.controlador_atendimento.seleciona_atendimento()
        except AtendimentoNaoEncontradoException as e:
            self.__tela.mostra_mensagem(str(e))
            return
        self.incluir(atendimento)

    def incluir(self, atendimento):
        dados = self.__tela.pega_dados()
        try:
            self.__valida_dados(dados)
            profissional = self.__busca_profissional(dados["cpf_profissional"])

            atendimento.adiciona_procedimento(dados["descricao"].strip(),
                                              dados["custo"], profissional)
            self.__tela.mostra_mensagem("Procedimento registrado com sucesso")
        except excecoes_procedimento as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            atendimento = self.__controlador_sistema.controlador_atendimento.seleciona_atendimento()
            procedimento = self.__seleciona_procedimento(atendimento)

            dados = self.__tela.pega_dados()
            self.__valida_dados(dados)
            profissional = self.__busca_profissional(dados["cpf_profissional"])

            novo_total = atendimento.calcular_valor_total() - procedimento.custo + dados["custo"]
            self.__controlador_sistema.controlador_pagamento.valida_novo_total(atendimento, novo_total)

            procedimento.descricao = dados["descricao"].strip()
            procedimento.custo = dados["custo"]
            procedimento.profissional = profissional
            self.__tela.mostra_mensagem("Procedimento alterado com sucesso")
        except excecoes_procedimento as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            atendimento = self.__controlador_sistema.controlador_atendimento.seleciona_atendimento()
            procedimento = self.__seleciona_procedimento(atendimento)

            novo_total = atendimento.calcular_valor_total() - procedimento.custo
            self.__controlador_sistema.controlador_pagamento.valida_novo_total(atendimento, novo_total)

            atendimento.remove_procedimento(procedimento)
            self.__tela.mostra_mensagem("Procedimento excluído com sucesso")
        except excecoes_procedimento as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not self.todos_procedimentos():
            self.__tela.mostra_mensagem("Nenhum procedimento registrado")
            return
        for atendimento in atendimentos:
            self.__mostra_do_atendimento(atendimento)

    def abre_tela(self):
        opcoes = {1: self.__seleciona_atendimento_e_incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()