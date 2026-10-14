from datetime import datetime
from tela.tela_abstrata import TelaAbstrata

class TelaAtendimento(TelaAbstrata):
    def mostra_menu(self) -> int:
        print("\n--- ATENDIMENTOS ---")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return self.le_inteiro("Escolha: ", [0, 1, 2, 3, 4])

    def pega_dados(self) -> dict:
        cpf_paciente = input("CPF do paciente: ")
        cpf_profissional = input("CPF do profissional: ")
        nome_clinica = input("Nome da clínica: ")
        nome_tipo = input("Tipo de atendimento: ")
        data = self.le_data("Data do atendimento (dd/mm/aaaa): ")
        hora_inicio = self.le_hora("Horário de início (hh:mm): ")
        hora_fim = self.le_hora("Horário de fim (hh:mm): ")
        valor = self.le_float("Valor: ")
        return {
            "cpf_paciente": cpf_paciente,
            "cpf_profissional": cpf_profissional,
            "nome_clinica": nome_clinica,
            "nome_tipo": nome_tipo,
            "horario_inicio": datetime.combine(data, hora_inicio),
            "horario_fim": datetime.combine(data, hora_fim),
            "valor": valor,
        }

    def mostra_dados(self, dados: dict):
        print(f"[{dados['numero']}] {dados['horario_inicio'].strftime('%d/%m/%Y %H:%M')}"
              f" até {dados['horario_fim'].strftime('%H:%M')}"
              f" | Clínica: {dados['clinica']}"
              f" | Paciente: {dados['paciente']}"
              f" | Profissional: {dados['profissional']}"
              f" | Tipo: {dados['tipo']}"
              f" | Valor: R$ {dados['valor']:.2f}")

    def seleciona(self) -> int:
        return self.le_inteiro("Número do atendimento: ")