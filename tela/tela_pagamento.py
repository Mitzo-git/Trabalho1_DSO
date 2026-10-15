from tela.tela_abstrata import TelaAbstrata

class TelaPagamento(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- PAGAMENTOS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        print("Forma de pagamento: 1 - Dinheiro | 2 - PIX | 3 - Cartão de crédito")
        opcao = self.le_inteiro("Escolha: ", [1, 2, 3])
        data = self.le_data("Data do pagamento (dd/mm/aaaa): ")
        valor_pago = self.le_float("Valor pago: ")

        dados = {"forma": {1: "dinheiro", 2: "pix", 3: "cartao"}[opcao],
                 "data": data, "valor_pago": valor_pago}
        if opcao == 2:
            dados["cpf_pagador"] = input("CPF do pagador (só números): ")
        elif opcao == 3:
            dados["numero_cartao"] = input("Número do cartão (só números): ")
            dados["bandeira"] = input("Bandeira: ")
        return dados

    def mostra_resumo(self, dados: dict):
        print(f"Total (atendimento + procedimentos): R$ {dados['valor_total']:.2f}"
              f" | Já pago: R$ {dados['valor_pago']:.2f}"
              f" | Restante: R$ {dados['valor_restante']:.2f}")

    def mostra_dados(self, dados: dict):
        print(f"[{dados['numero']}] {dados['data'].strftime('%d/%m/%Y')}"
              f" | {dados['forma']}"
              f" | Paciente: {dados['paciente']}"
              f" | Atendimento: {dados['horario_atendimento'].strftime('%d/%m/%Y %H:%M')}"
              f" | Pago: R$ {dados['valor_pago']:.2f}"
              f" | Restante do atendimento: R$ {dados['valor_restante']:.2f}")

    def seleciona(self) -> int:
        return self.le_inteiro("Número do pagamento: ")