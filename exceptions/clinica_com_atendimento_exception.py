class ClinicaComAtendimentoException(Exception):
    def __init__(self):
        super().__init__("A clínica possui atendimentos e não pode ser excluída")