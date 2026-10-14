from datetime import datetime, time, date

class TelaAbstrata:
    #leituras simples sem regras de negocio
    def le_inteiro(self, mensagem: str, opcoes: list = None) -> int:
        while True:
            try:
                valor = int(input(mensagem))
            except ValueError:
                print("Digite um número inteiro.")
                continue
            if opcoes is not None and valor not in opcoes:
                print(f"Opção inválida. Escolha entre: {opcoes}")
                continue
            return valor

    def le_float(self, mensagem: str) -> float:
        while True:
            texto = input(mensagem).replace(",", ".")
            try:
                return float(texto)
            except ValueError:
                print("Valor inválido. Use números, por exemplo 150.50")

    #leitura data de nascimento
    def le_data(self, mensagem: str):
        while True:
            texto = input(mensagem)
            try:
                return datetime.strptime(texto, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa, por exemplo 17/05/2000.")

    def le_hora(self, mensagem: str) -> time:
        while True:
            texto = input(mensagem)
            try:
                return datetime.strptime(texto, "%H:%M").time()
            except ValueError:
                print("Horário inválido. Use o formato hh:mm, por exemplo 14:30.")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)