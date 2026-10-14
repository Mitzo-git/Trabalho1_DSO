from tela.tela_abstrata import TelaAbstrata

class TelaProfissional(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- PROFISSIONAIS DE SAÚDE ---")
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
        especialidade = input("Especialidade: ")
        registro = input("Registro profissional: ")
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "especialidade": especialidade,
            "registro": registro,
        }

    def mostra_dados(self, dados: dict):
        print(f"Nome: {dados['nome']} | CPF: {dados['cpf']}"
              f" | Celular: {dados['celular']}"
              f" | Especialidade: {dados['especialidade']}"
              f" | Registro: {dados['registro']}")

    def seleciona(self) -> str:
        return input("CPF do profissional: ")