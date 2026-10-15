class RelatorioSemDadosException(Exception):
    def __init__(self, mensagem: str = "Não há dados suficientes para gerar o relatório"):
        super().__init__(mensagem)