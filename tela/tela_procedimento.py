from tela.tela_abstrata import TelaAbstrata

class TelaProcedimento(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- PROCEDIMENTOS ---")
        print("1 - Incluir (em um atendimento)")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        descricao = input("Descrição do procedimento: ")
        custo = self.le_float("Custo: ")
        cpf_profissional = input("CPF do profissional responsável: ")
        return {"descricao": descricao, "custo": custo,
                "cpf_profissional": cpf_profissional}

    def mostra_dados(self, dados: dict):
        print(f"Atendimento [{dados['numero_atendimento']}] "
              f"{dados['paciente']} em {dados['horario_atendimento'].strftime('%d/%m/%Y %H:%M')}"
              f" -> ({dados['numero']}) {dados['descricao']}"
              f" | Custo: R$ {dados['custo']:.2f}"
              f" | Profissional: {dados['profissional']}")

    def seleciona(self) -> int:
        return self.le_inteiro("Número do procedimento: ")