from entidade.atendimento import Atendimento
from tela.tela_atendimento import TelaAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.paciente_nao_encontrado_exception import PacienteNaoEncontradoException
from exceptions.profissional_nao_encontrado_exception import ProfissionalNaoEncontradoException
from exceptions.clinica_nao_encontrada_exception import ClinicaNaoEncontradaException
from exceptions.tipo_atendimento_nao_encontrado_exception import TipoAtendimentoNaoEncontradoException
from exceptions.atendimento_nao_encontrado_exception import AtendimentoNaoEncontradoException
from exceptions.paciente_menor_de_idade_exception import PacienteMenorDeIdadeException
from exceptions.fora_do_horario_exception import ForaDoHorarioException
from exceptions.atendimento_com_pagamento_exception import AtendimentoComPagamentoException
from exceptions.valor_total_menor_que_pago_exception import ValorTotalMenorQuePagoException

idade_minima = 18

excecoes_atendimento = (
    DadoInvalidoException,
    PacienteNaoEncontradoException,
    ProfissionalNaoEncontradoException,
    ClinicaNaoEncontradaException,
    TipoAtendimentoNaoEncontradoException,
    AtendimentoNaoEncontradoException,
    PacienteMenorDeIdadeException,
    ForaDoHorarioException,
    AtendimentoComPagamentoException,
    ValorTotalMenorQuePagoException,
)

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__atendimentos = []
        self.__tela = TelaAtendimento()
        self.__controlador_sistema = controlador_sistema

    @property
    def atendimentos(self):
        return list(self.__atendimentos)  # usado por Pagamento, Procedimento e Relatório

    def pega_atendimento_por_numero(self, numero: int):
        if 1 <= numero <= len(self.__atendimentos):
            return self.__atendimentos[numero - 1]
        return None

    def seleciona_atendimento(self):
        if not self.__atendimentos:
            raise AtendimentoNaoEncontradoException()
        self.listar()
        atendimento = self.pega_atendimento_por_numero(self.__tela.seleciona())
        if atendimento is None:
            raise AtendimentoNaoEncontradoException()
        return atendimento

    # associação: pede os objetos aos outros controladores
    def __busca_participantes(self, dados: dict):
        sistema = self.__controlador_sistema

        paciente = sistema.controlador_paciente.pega_paciente_por_cpf(dados["cpf_paciente"])
        if paciente is None:
            raise PacienteNaoEncontradoException()

        profissional = sistema.controlador_profissional.pega_profissional_por_cpf(dados["cpf_profissional"])
        if profissional is None:
            raise ProfissionalNaoEncontradoException()

        clinica = sistema.controlador_clinica.pega_clinica_por_nome(dados["nome_clinica"])
        if clinica is None:
            raise ClinicaNaoEncontradaException()

        tipo = sistema.controlador_tipo_atendimento.pega_tipo_por_nome(dados["nome_tipo"])
        if tipo is None:
            raise TipoAtendimentoNaoEncontradoException()

        return paciente, profissional, clinica, tipo

    # ---------- regras de negócio ----------
    def __valida_regras(self, paciente, clinica, inicio, fim, valor):
        if fim <= inicio:
            raise DadoInvalidoException("O horário de fim deve ser depois do início")
        if valor < 0:
            raise DadoInvalidoException("O valor não pode ser negativo")

        # Regra 1: idade
        if paciente.calcula_idade() < idade_minima:
            raise PacienteMenorDeIdadeException()

        # Regra 2: dentro do funcionamento da clínica
        if (inicio.time() < clinica.horario_abertura
                or fim.time() > clinica.horario_fechamento):
            raise ForaDoHorarioException(clinica.horario_abertura, clinica.horario_fechamento)

    def incluir(self):
        dados = self.__tela.pega_dados()
        try:
            paciente, profissional, clinica, tipo = self.__busca_participantes(dados)
            self.__valida_regras(paciente, clinica, dados["horario_inicio"],
                                 dados["horario_fim"], dados["valor"])

            atendimento = Atendimento(dados["horario_inicio"], dados["horario_fim"],
                                      dados["valor"], tipo, paciente, profissional, clinica)
            self.__atendimentos.append(atendimento)
            clinica.adiciona_atendimento(atendimento)  # agregação
            self.__tela.mostra_mensagem("Atendimento cadastrado com sucesso")
        except excecoes_atendimento as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            atendimento = self.seleciona_atendimento()
            dados = self.__tela.pega_dados()
            paciente, profissional, clinica, tipo = self.__busca_participantes(dados)
            self.__valida_regras(paciente, clinica, dados["horario_inicio"],
                                 dados["horario_fim"], dados["valor"])

            # o novo total (valor base + procedimentos) não pode ficar abaixo do que já foi pago
            novo_total = dados["valor"] + sum(p.custo for p in atendimento.procedimentos)
            self.__controlador_sistema.controlador_pagamento.valida_novo_total(atendimento, novo_total)

            if atendimento.clinica is not clinica:
                atendimento.clinica.remove_atendimento(atendimento)
                clinica.adiciona_atendimento(atendimento)
                atendimento.clinica = clinica

            atendimento.paciente = paciente
            atendimento.profissional = profissional
            atendimento.tipo_de_atendimento = tipo
            atendimento.altera_horarios(dados["horario_inicio"], dados["horario_fim"])
            atendimento.valor = dados["valor"]
            self.__tela.mostra_mensagem("Atendimento alterado com sucesso")
        except excecoes_atendimento as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            atendimento = self.seleciona_atendimento()

            pagamentos = self.__controlador_sistema.controlador_pagamento.pega_pagamentos_do_atendimento(atendimento)
            if len(pagamentos) > 0:
                raise AtendimentoComPagamentoException()

            atendimento.clinica.remove_atendimento(atendimento)
            self.__atendimentos.remove(atendimento)
            self.__tela.mostra_mensagem("Atendimento excluído com sucesso")
        except excecoes_atendimento as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__atendimentos:
            self.__tela.mostra_mensagem("Nenhum atendimento cadastrado")
            return
        for numero, atendimento in enumerate(self.__atendimentos, start=1):
            self.__tela.mostra_dados({
                "numero": numero,
                "clinica": atendimento.clinica.nome,
                "paciente": atendimento.paciente.nome,
                "profissional": atendimento.profissional.nome,
                "tipo": atendimento.tipo_de_atendimento.nome,
                "horario_inicio": atendimento.horario_inicio,
                "horario_fim": atendimento.horario_fim,
                "valor": atendimento.valor,
            })

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()