from tela.tela_abstrata import TelaAbstrata

class TelaRelatorio(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- RELATÓRIOS ---")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def mostra_ranking_clinicas(self, itens: list):
        print("\n=== CLÍNICAS COM MAIS ATENDIMENTOS ===")
        for item in itens:
            print(f"{item['posicao']}º | Clínica: {item['clinica']}"
                  f" | Cidade: {item['cidade']}"
                  f" | Atendimentos: {item['atendimentos']}")

    def mostra_ranking_atendimentos(self, titulo: str, itens: list):
        print(f"\n=== {titulo} ===")
        for item in itens:
            print(f"{item['posicao']}º | Clínica: {item['clinica']}"
                  f" | Paciente: {item['paciente']}"
                  f" | Profissional: {item['profissional']}"
                  f" | Tipo: {item['tipo']}"
                  f" | Início: {item['horario_inicio'].strftime('%d/%m/%Y %H:%M')}"
                  f" | Valor: R$ {item['valor']:.2f}")

    def mostra_ranking_procedimentos_realizados(self, itens: list):
        print("\n=== PROCEDIMENTOS MAIS REALIZADOS ===")
        for item in itens:
            print(f"{item['posicao']}º | Descrição: {item['descricao']}"
                  f" | Realizações: {item['quantidade']}")

    def mostra_ranking_procedimentos_valor(self, titulo: str, itens: list):
        print(f"\n=== {titulo} ===")
        for item in itens:
            print(f"{item['posicao']}º | Descrição: {item['descricao']}"
                  f" | Profissional: {item['profissional']}"
                  f" | Custo: R$ {item['custo']:.2f}")