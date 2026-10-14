from datetime import time

class ForaDoHorarioException(Exception):
    def __init__(self, abertura: time, fechamento: time):
        super().__init__(
            "O atendimento deve ocorrer dentro do horário de funcionamento da clínica "
            f"({abertura.strftime('%H:%M')} às {fechamento.strftime('%H:%M')})"
        )