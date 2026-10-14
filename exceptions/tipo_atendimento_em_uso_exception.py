class TipoAtendimentoEmUsoException(Exception):
    def __init__(self):
        super().__init__("O tipo de atendimento está em uso por atendimentos e não pode ser excluído")