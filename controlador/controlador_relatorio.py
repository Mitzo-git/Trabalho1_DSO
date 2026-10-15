from tela.tela_relatorio import TelaRelatorio
from exceptions.relatorio_sem_dados_exception import RelatorioSemDadosException

# quantos itens aparecem em cada ranking.
TOP = 5


class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__tela = TelaRelatorio()
        self.__controlador_sistema = controlador_sistema

    def __busca_atendimentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if len(atendimentos) == 0:
            raise RelatorioSemDadosException("Não há atendimentos cadastrados para gerar o relatório")
        return atendimentos

    def __busca_procedimentos(self):
        procedimentos = self.__controlador_sistema.controlador_procedimento.todos_procedimentos()
        if len(procedimentos) == 0:
            raise RelatorioSemDadosException("Não há procedimentos registrados para gerar o relatório")
        return procedimentos

    def __ordem(self, valores: list, decrescente: bool) -> list:
        restantes = list(range(len(valores)))
        ordem = []
        while len(restantes) > 0:
            melhor = restantes[0]
            for posicao in restantes:
                if decrescente and valores[posicao] > valores[melhor]:
                    melhor = posicao
                if not decrescente and valores[posicao] < valores[melhor]:
                    melhor = posicao
            ordem.append(melhor)
            restantes.remove(melhor)
        return ordem

    def __itens_atendimentos(self, atendimentos: list, ordem: list) -> list:
        itens = []
        quantidade = min(TOP, len(ordem))
        for i in range(quantidade):
            atendimento = atendimentos[ordem[i]]
            itens.append({
                "posicao": i + 1,
                "clinica": atendimento.clinica.nome,
                "paciente": atendimento.paciente.nome,
                "profissional": atendimento.profissional.nome,
                "tipo": atendimento.tipo_de_atendimento.nome,
                "horario_inicio": atendimento.horario_inicio,
                "valor": atendimento.valor,
            })
        return itens

    def __itens_procedimentos(self, procedimentos: list, ordem: list) -> list:
        itens = []
        quantidade = min(TOP, len(ordem))
        for i in range(quantidade):
            procedimento = procedimentos[ordem[i]]
            itens.append({
                "posicao": i + 1,
                "descricao": procedimento.descricao,
                "profissional": procedimento.profissional.nome,
                "custo": procedimento.custo,
            })
        return itens

    def clinicas_mais_atendimentos(self):
        try:
            self.__busca_atendimentos()
            clinicas = self.__controlador_sistema.controlador_clinica.clinicas

            totais = []
            for clinica in clinicas:
                totais.append(len(clinica.atendimentos))

            ordem = self.__ordem(totais, True)
            itens = []
            quantidade = min(TOP, len(ordem))
            for i in range(quantidade):
                clinica = clinicas[ordem[i]]
                itens.append({
                    "posicao": i + 1,
                    "clinica": clinica.nome,
                    "cidade": clinica.cidade,
                    "atendimentos": totais[ordem[i]],
                })
            self.__tela.mostra_ranking_clinicas(itens)
        except RelatorioSemDadosException as e:
            self.__tela.mostra_mensagem(str(e))

    def atendimentos_mais_caros_e_baratos(self):
        try:
            atendimentos = self.__busca_atendimentos()

            valores = []
            for atendimento in atendimentos:
                valores.append(atendimento.valor)

            mais_caros = self.__itens_atendimentos(atendimentos, self.__ordem(valores, True))
            mais_baratos = self.__itens_atendimentos(atendimentos, self.__ordem(valores, False))
            self.__tela.mostra_ranking_atendimentos("ATENDIMENTOS MAIS CAROS", mais_caros)
            self.__tela.mostra_ranking_atendimentos("ATENDIMENTOS MAIS BARATOS", mais_baratos)
        except RelatorioSemDadosException as e:
            self.__tela.mostra_mensagem(str(e))

    def procedimentos_mais_realizados(self):
        try:
            procedimentos = self.__busca_procedimentos()

            descricoes = []
            quantidades = []

            for procedimento in procedimentos:
                nome = procedimento.descricao.strip()
                encontrou = False
                for i in range(len(descricoes)):
                    if descricoes[i].lower() == nome.lower():
                        quantidades[i] = quantidades[i] + 1
                        encontrou = True
                if not encontrou:
                    descricoes.append(nome)
                    quantidades.append(1)

            ordem = self.__ordem(quantidades, True)
            itens = []
            quantidade = min(TOP, len(ordem))
            for i in range(quantidade):
                itens.append({
                    "posicao": i + 1,
                    "descricao": descricoes[ordem[i]],
                    "quantidade": quantidades[ordem[i]],
                })
            self.__tela.mostra_ranking_procedimentos_realizados(itens)
        except RelatorioSemDadosException as e:
            self.__tela.mostra_mensagem(str(e))

    def procedimentos_mais_caros_e_baratos(self):
        try:
            procedimentos = self.__busca_procedimentos()

            custos = []
            for procedimento in procedimentos:
                custos.append(procedimento.custo)

            mais_caros = self.__itens_procedimentos(procedimentos, self.__ordem(custos, True))
            mais_baratos = self.__itens_procedimentos(procedimentos, self.__ordem(custos, False))
            self.__tela.mostra_ranking_procedimentos_valor("PROCEDIMENTOS MAIS CAROS", mais_caros)
            self.__tela.mostra_ranking_procedimentos_valor("PROCEDIMENTOS MAIS BARATOS", mais_baratos)
        except RelatorioSemDadosException as e:
            self.__tela.mostra_mensagem(str(e))

    def abre_tela(self):
        opcoes = {1: self.clinicas_mais_atendimentos,
                  2: self.atendimentos_mais_caros_e_baratos,
                  3: self.procedimentos_mais_realizados,
                  4: self.procedimentos_mais_caros_e_baratos}
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao == 0:
                break
            opcoes[opcao]()