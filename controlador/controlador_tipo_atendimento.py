from entidade.tipo_atendimento import TipoAtendimento
from tela.tela_tipo_atendimento import TelaTipoAtendimento
from exceptions.dado_invalido_exception import DadoInvalidoException
from exceptions.tipo_atendimento_ja_cadastrado_exception import TipoAtendimentoJaCadastradoException
from exceptions.tipo_atendimento_nao_encontrado_exception import TipoAtendimentoNaoEncontradoException
from exceptions.tipo_atendimento_em_uso_exception import TipoAtendimentoEmUsoException

excecoes_tipo = (
    DadoInvalidoException,
    TipoAtendimentoJaCadastradoException,
    TipoAtendimentoNaoEncontradoException,
    TipoAtendimentoEmUsoException,
)

class ControladorTipoAtendimento:
    def __init__(self, controlador_sistema):
        self.__tipos = []
        self.__tela = TelaTipoAtendimento()
        self.__controlador_sistema = controlador_sistema

    @property
    def tipos(self):
        return list(self.__tipos)

    def pega_tipo_por_nome(self, nome: str):
        nome = nome.strip().lower()
        for tipo in self.__tipos:
            if tipo.nome.strip().lower() == nome:
                return tipo
        return None

    def __valida_dados(self, dados: dict):
        if not dados["nome"].strip():
            raise DadoInvalidoException("O nome do tipo não pode ser vazio")

    def __seleciona_tipo(self):
        if not self.__tipos:
            raise TipoAtendimentoNaoEncontradoException()
        self.listar()
        tipo = self.pega_tipo_por_nome(self.__tela.seleciona())
        if tipo is None:
            raise TipoAtendimentoNaoEncontradoException()
        return tipo

    def __esta_em_uso(self, tipo) -> bool:
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        return any(a.tipo_de_atendimento is tipo for a in atendimentos)

    def incluir(self):
        dados = self.__tela.pega_dados()
        try:
            self.__valida_dados(dados)
            if self.pega_tipo_por_nome(dados["nome"]) is not None:
                raise TipoAtendimentoJaCadastradoException()

            self.__tipos.append(TipoAtendimento(dados["nome"].strip()))
            self.__tela.mostra_mensagem("Tipo de atendimento cadastrado com sucesso")
        except excecoes_tipo as e:
            self.__tela.mostra_mensagem(str(e))

    def alterar(self):
        try:
            tipo = self.__seleciona_tipo()
            dados = self.__tela.pega_dados()
            self.__valida_dados(dados)

            outro = self.pega_tipo_por_nome(dados["nome"])
            if outro is not None and outro is not tipo:
                raise TipoAtendimentoJaCadastradoException()

            tipo.nome = dados["nome"].strip()
            self.__tela.mostra_mensagem("Tipo de atendimento alterado com sucesso")
        except excecoes_tipo as e:
            self.__tela.mostra_mensagem(str(e))

    def excluir(self):
        try:
            tipo = self.__seleciona_tipo()
            if self.__esta_em_uso(tipo):
                raise TipoAtendimentoEmUsoException()
            self.__tipos.remove(tipo)
            self.__tela.mostra_mensagem("Tipo de atendimento excluído com sucesso")
        except excecoes_tipo as e:
            self.__tela.mostra_mensagem(str(e))

    def listar(self):
        if not self.__tipos:
            self.__tela.mostra_mensagem("Nenhum tipo de atendimento cadastrado")
            return
        for tipo in self.__tipos:
            self.__tela.mostra_dados({"nome": tipo.nome})

    def abre_tela(self):
        opcoes = {1: self.incluir, 2: self.alterar,
                  3: self.excluir, 4: self.listar}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()