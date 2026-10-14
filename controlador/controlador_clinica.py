from entidade.clinica import Clinica
from tela.tela_clinica import TelaClinica
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.clinica_ja_cadastrada_exception import ClinicaJaCadastradaException
from exceptions.clinica_nao_encontrada_exception import ClinicaNaoEncontradaException
from exceptions.clinica_com_atendimento_exception import ClinicaComAtendimentoException

excecoes_clinica = (
    DadoInvalidoException,
    ClinicaJaCadastradaException,
    ClinicaNaoEncontradaException,
    ClinicaComAtendimentoException,
)

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__clinicas = []
        self.__tela = TelaClinica()
        self.__controlador_sistema = controlador_sistema

    @property
    def clinicas(self):
        return list(self.__clinicas)  # usado pelo ControladorRelatorio

    def pega_clinica_por_nome(self, nome: str):
        nome = nome.strip().lower()
        for clinica in self.__clinicas:
            if clinica.nome.strip().lower() == nome:
                return clinica
        return None

    def __valida_dados(self, dados: dict):
        if not dados["nome"].strip():
            raise DadoInvalidoException("O nome não pode ser vazio")
        if not dados["cidade"].strip():
            raise DadoInvalidoException("A cidade não pode ser vazia")
        if not dados["descricao"].strip():
            raise DadoInvalidoException("A descrição não pode ser vazia")
        if dados["horario_abertura"] >= dados["horario_fechamento"]:
            raise DadoInvalidoException("O horário de abertura deve ser antes do fechamento")

    def __seleciona_clinica(self):
        if not self.__clinicas:
            raise ClinicaNaoEncontradaException()
        self.listar()
        clinica = self.pega_clinica_por_nome(self.__tela.seleciona())
        if clinica is None:
            raise ClinicaNaoEncontradaException()
        return clinica

    def incluir(self):
        dados = self.__tela.pega_dados()
        try:
            self.__valida_dados(dados)
            if self.pega_clinica_por_nome(dados["nome"]) is not None:
                raise ClinicaJaCadastradaException()

            clinica = Clinica(dados["nome"].strip(), dados["cidade"].strip(),
                              dados["descricao"].strip(),
                              dados["horario_abertura"], dados["horario_fechamento"])
            self.__clinicas.append(clinica)
            self.__tela.mostra_mensagem("Clínica cadastrada com sucesso")
        except excecoes_clinica as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            clinica = self.__seleciona_clinica()
            dados = self.__tela.pega_dados()
            self.__valida_dados(dados)

            # o novo nome não pode ser de outra clínica
            outra = self.pega_clinica_por_nome(dados["nome"])
            if outra is not None and outra is not clinica:
                raise ClinicaJaCadastradaException()

            # novo horário não pode deixar atendimentos já marcados fora do funcionamento
            for atendimento in clinica.atendimentos:
                if (atendimento.horario_inicio.time() < dados["horario_abertura"]
                        or atendimento.horario_fim.time() > dados["horario_fechamento"]):
                    raise DadoInvalidoException(
                        "Existem atendimentos marcados fora do novo horário de funcionamento")

            clinica.nome = dados["nome"].strip()
            clinica.cidade = dados["cidade"].strip()
            clinica.descricao = dados["descricao"].strip()
            clinica.horario_abertura = dados["horario_abertura"]
            clinica.horario_fechamento = dados["horario_fechamento"]
            self.__tela.mostra_mensagem("Clínica alterada com sucesso")
        except excecoes_clinica as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            clinica = self.__seleciona_clinica()
            if clinica.atendimentos:
                raise ClinicaComAtendimentoException()
            self.__clinicas.remove(clinica)
            self.__tela.mostra_mensagem("Clínica excluída com sucesso")
        except excecoes_clinica as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__clinicas:
            self.__tela.mostra_mensagem("Nenhuma clínica cadastrada")
            return
        for clinica in self.__clinicas:
            self.__tela.mostra_dados({
                "nome": clinica.nome,
                "cidade": clinica.cidade,
                "descricao": clinica.descricao,
                "horario_abertura": clinica.horario_abertura,
                "horario_fechamento": clinica.horario_fechamento,
                "total_atendimentos": len(clinica.atendimentos),
            })

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()