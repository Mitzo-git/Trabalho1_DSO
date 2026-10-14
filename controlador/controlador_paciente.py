from datetime import date
from entidade.paciente import Paciente
from tela.tela_paciente import TelaPaciente
from exceptions.paciente_ja_cadastrado_exception import PacienteJaCadastradoException
from exceptions.paciente_nao_encontrado_exception import PacienteNaoEncontradoException
from exceptions.dado_invalido_exception import DadoInvalidoException


class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela = TelaPaciente()
        self.__controlador_sistema = controlador_sistema

    def pega_paciente_por_cpf(self, cpf: str):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def __valida_dados(self, dados: dict):
        if not dados["nome"].strip():
            raise DadoInvalidoException("O nome não pode ser vazio")
        if not dados["cpf"].isdigit() or len(dados["cpf"]) != 11:
            raise DadoInvalidoException("CPF deve ter 11 dígitos numéricos")
        if not dados["celular"].isdigit() or len(dados["celular"]) < 10:
            raise DadoInvalidoException("Celular inválido (use apenas números com DDD)")
        if dados["data_de_nascimento"] > date.today():
            raise DadoInvalidoException("Data de nascimento não pode ser no futuro")

    def incluir(self):
        dados = self.__tela.pega_dados()
        if dados is None:
            return
        try:
            self.__valida_dados(dados)
            if self.pega_paciente_por_cpf(dados["cpf"]) is not None:
                raise PacienteJaCadastradoException()

            paciente = Paciente(dados["nome"], dados["celular"],
                                dados["cpf"], dados["data_de_nascimento"])
            self.__pacientes.append(paciente)
            self.__tela.mostra_mensagem("Paciente cadastrado com sucesso")
        except (DadoInvalidoException, PacienteJaCadastradoException) as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        self.listar()
        cpf = self.__tela.seleciona()
        try:
            paciente = self.pega_paciente_por_cpf(cpf)
            if paciente is None:
                raise PacienteNaoEncontradoException()

            novos_dados = self.__tela.pega_dados()
            if novos_dados is None:
                return
            self.__valida_dados(novos_dados)

            outro = self.pega_paciente_por_cpf(novos_dados["cpf"])
            if outro is not None and outro is not paciente:
                raise PacienteJaCadastradoException()

            paciente.nome = novos_dados["nome"]
            paciente.celular = novos_dados["celular"]
            paciente.cpf = novos_dados["cpf"]
            paciente.data_de_nascimento = novos_dados["data_de_nascimento"]
            self.__tela.mostra_mensagem("Paciente alterado com sucesso")
        except (PacienteNaoEncontradoException, DadoInvalidoException,
                PacienteJaCadastradoException) as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        self.listar()
        cpf = self.__tela.seleciona()
        try:
            paciente = self.pega_paciente_por_cpf(cpf)
            if paciente is None:
                raise PacienteNaoEncontradoException()
            self.__pacientes.remove(paciente)
            self.__tela.mostra_mensagem("Paciente excluído com sucesso")
        except PacienteNaoEncontradoException as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__pacientes:
            self.__tela.mostra_mensagem("Nenhum paciente cadastrado")
            return
        for paciente in self.__pacientes:
            self.__tela.mostra_dados({
                "nome": paciente.nome,
                "celular": paciente.celular,
                "cpf": paciente.cpf,
                "data_de_nascimento": paciente.data_de_nascimento,
            })

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()