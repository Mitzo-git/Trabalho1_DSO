from tela.tela_abstrata import TelaAbstrata

class TelaPaciente(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- PACIENTES ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        nome = input("Nome: ")
        celular = input("Celular com DDD (só números): ")
        cpf = input("CPF (só números): ")
        data_de_nascimento = self.le_data("Data de nascimento (dd/mm/aaaa): ")
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "data_de_nascimento": data_de_nascimento,
        }

    def mostra_dados(self, dados: dict):
        print(f"Nome: {dados['nome']} | CPF: {dados['cpf']}"
              f" | Celular: {dados['celular']}"
              f" | Nascimento: {dados['data_de_nascimento'].strftime('%d/%m/%Y')}")

    def seleciona(self) -> str:
        return input("CPF do paciente: ")