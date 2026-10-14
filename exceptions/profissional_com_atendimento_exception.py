class ProfissionalComAtendimentoException(Exception):
    def __init__(self):
        super().__init__("O profissional possui atendimentos ou procedimentos e não pode ser excluído")