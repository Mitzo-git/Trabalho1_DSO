from controlador.controlador_paciente import controlador_paciente
from controlador.controlador_profissional import controlador_profissional
from controlador.controlador_clinica import controlador_clinica
from controlador.controlador_tipo_atendimento import controlador_tipo_atendimento
from controlador.controlador_atendimento import controlador_atendimento
from controlador.controlador_procedimento import controlador_procedimento
from controlador.controlador_pagamento import controlador_pagamento
from controlador.controlador_relatorio import controlador_relatorio
from tela.tela_sistema import tela_sistema


class ControladorSistema:
    def __init__(self):
        self.__tela = tela_sistema()

        self.__controlador_paciente = controlador_paciente(self)
        self.__controlador_profissional = controlador_profissional(self)
        self.__controlador_clinica = controlador_clinica(self)
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento(self)
        self.__controlador_atendimento = controlador_atendimento(self)
        self.__controlador_procedimento = controlador_procedimento(self)
        self.__controlador_pagamento = controlador_pagamento(self)
        self.__controlador_relatorio = controlador_relatorio(self)

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_procedimento(self):
        return self.__controlador_procedimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        self.abre_tela()
        self.encerra_sistema()

    def abre_tela(self):
        opcoes = {
            1: self.__controlador_paciente.abre_tela,
            2: self.__controlador_profissional.abre_tela,
            3: self.__controlador_clinica.abre_tela,
            4: self.__controlador_tipo_atendimento.abre_tela,
            5: self.__controlador_atendimento.abre_tela,
            6: self.__controlador_procedimento.abre_tela,
            7: self.__controlador_pagamento.abre_tela,
            8: self.__controlador_relatorio.abre_tela,
            0: self.encerra_sistema,
        }
        while True:
            opcao = self.__tela.mostra_menu_principal()
            if opcao == 0:
                break
            opcoes[opcao]()

    def encerra_sistema(self):
        self.__tela.mostra_mensagem("Encerrando o sistema. ")