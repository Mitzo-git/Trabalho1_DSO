class PacienteComAtendimentoException(Exception):
    def __init__(self):
        super().__init__("O paciente possui atendimentos e não pode ser excluído")