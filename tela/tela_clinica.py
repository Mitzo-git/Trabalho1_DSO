from tela.tela_abstrata import TelaAbstrata

class TelaClinica(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- CLÍNICAS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        nome = input("Nome da clínica: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        horario_abertura = self.le_hora("Horário de abertura (hh:mm): ")
        horario_fechamento = self.le_hora("Horário de fechamento (hh:mm): ")
        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento,
        }

    def mostra_dados(self, dados: dict):
        print(f"Clínica: {dados['nome']} | Cidade: {dados['cidade']}"
              f" | Funcionamento: {dados['horario_abertura'].strftime('%H:%M')}"
              f" às {dados['horario_fechamento'].strftime('%H:%M')}"
              f" | Atendimentos: {dados['total_atendimentos']}")
        print(f"   {dados['descricao']}")

    def seleciona(self) -> str:
        return input("Nome da clínica: ")