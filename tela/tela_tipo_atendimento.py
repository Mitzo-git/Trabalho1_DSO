from tela.tela_abstrata import TelaAbstrata

class TelaTipoAtendimento(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- TIPOS DE ATENDIMENTO ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        nome = input("Nome do tipo (ex.: consulta, exame, retorno): ")
        return {"nome": nome}

    def mostra_dados(self, dados: dict):
        print(f"Tipo: {dados['nome']}")

    def seleciona(self) -> str:
        return input("Nome do tipo de atendimento: ")