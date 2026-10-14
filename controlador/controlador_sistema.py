from controlador.controlador_paciente import ControladorPaciente
from controlador.controlador_profissional import ControladorProfissional
from controlador.controlador_clinica import ControladorClinica
from controlador.controlador_tipo_atendimento import ControladorTipoAtendimento
from controlador.controlador_atendimento import ControladorAtendimento
from controlador.controlador_procedimento import ControladorProcedimento
from controlador.controlador_pagamento import ControladorPagamento
from controlador.controlador_relatorio import ControladorRelatorio
from tela.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela = TelaSistema()

        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_procedimento = ControladorProcedimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_relatorio = ControladorRelatorio(self)

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