from tela.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    def mostra_menu_principal(self) -> int:
        print("\n===== SISTEMA DE CLÍNICAS =====")
        print("--- Cadastros ---")
        print("1 - Pacientes")
        print("2 - Profissionais de saúde")
        print("3 - Clínicas")
        print("4 - Tipos de atendimento")
        print("--- Registros ---")
        print("5 - Atendimentos")
        print("6 - Procedimentos")
        print("7 - Pagamentos")
        print("--- Relatórios ---")
        print("8 - Relatórios")
        print("0 - Sair")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4, 5, 6, 7, 8])