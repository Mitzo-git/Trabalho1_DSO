from entidade.profissional_da_saude import ProfissionalDaSaude
from tela.tela_profissional import TelaProfissional
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.profissional_ja_cadastrado_exception import ProfissionalJaCadastradoException
from exceptions.profissional_nao_encontrado_exception import ProfissionalNaoEncontradoException
from exceptions.profissional_com_atendimento_exception import ProfissionalComAtendimentoException

excecoes_profissional = (
    DadoInvalidoException,
    ProfissionalJaCadastradoException,
    ProfissionalNaoEncontradoException,
    ProfissionalComAtendimentoException,
)


class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__profissionais = []
        self.__tela = TelaProfissional()
        self.__controlador_sistema = controlador_sistema

    @property
    def profissionais(self):
        return list(self.__profissionais)

    def pega_profissional_por_cpf(self, cpf: str):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    def __valida_dados(self, dados: dict):
        if not dados["nome"].strip():
            raise DadoInvalidoException("O nome não pode ser vazio")
        if not dados["cpf"].isdigit() or len(dados["cpf"]) != 11:
            raise DadoInvalidoException("CPF deve ter 11 dígitos numéricos")
        if not dados["celular"].isdigit() or len(dados["celular"]) < 10:
            raise DadoInvalidoException("Celular inválido (use apenas números com DDD)")
        if not dados["especialidade"].strip():
            raise DadoInvalidoException("A especialidade não pode ser vazia")
        if not dados["registro"].strip():
            raise DadoInvalidoException("O registro profissional não pode ser vazio")

    def __seleciona_profissional(self):
        if not self.__profissionais:
            raise ProfissionalNaoEncontradoException()
        self.listar()
        profissional = self.pega_profissional_por_cpf(self.__tela.seleciona())
        if profissional is None:
            raise ProfissionalNaoEncontradoException()
        return profissional

    def __tem_vinculos(self, profissional) -> bool:
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        for atendimento in atendimentos:
            if atendimento.profissional is profissional:
                return True
            for procedimento in atendimento.procedimentos:
                if procedimento.profissional is profissional:
                    return True
        return False

    def incluir(self):
        dados = self.__tela.pega_dados()
        try:
            self.__valida_dados(dados)
            if self.pega_profissional_por_cpf(dados["cpf"]) is not None:
                raise ProfissionalJaCadastradoException()

            profissional = ProfissionalDaSaude(dados["nome"].strip(), dados["celular"],
                                               dados["cpf"], dados["especialidade"].strip(),
                                               dados["registro"].strip())
            self.__profissionais.append(profissional)
            self.__tela.mostra_mensagem("Profissional cadastrado com sucesso")
        except excecoes_profissional as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            profissional = self.__seleciona_profissional()
            dados = self.__tela.pega_dados()
            self.__valida_dados(dados)

            outro = self.pega_profissional_por_cpf(dados["cpf"])
            if outro is not None and outro is not profissional:
                raise ProfissionalJaCadastradoException()

            profissional.nome = dados["nome"].strip()
            profissional.celular = dados["celular"]
            profissional.cpf = dados["cpf"]
            profissional.especialidade = dados["especialidade"].strip()
            profissional.registro = dados["registro"].strip()
            self.__tela.mostra_mensagem("Profissional alterado com sucesso")
        except excecoes_profissional as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            profissional = self.__seleciona_profissional()
            if self.__tem_vinculos(profissional):
                raise ProfissionalComAtendimentoException()
            self.__profissionais.remove(profissional)
            self.__tela.mostra_mensagem("Profissional excluído com sucesso")
        except excecoes_profissional as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__profissionais:
            self.__tela.mostra_mensagem("Nenhum profissional cadastrado")
            return
        for profissional in self.__profissionais:
            self.__tela.mostra_dados({
                "nome": profissional.nome,
                "celular": profissional.celular,
                "cpf": profissional.cpf,
                "especialidade": profissional.especialidade,
                "registro": profissional.registro,
            })

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()