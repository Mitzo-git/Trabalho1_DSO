from datetime import datetime

class TelaAbstrata:


    #leitura data de nascimento
    def le_data(self, mensagem: str):
        while True:
            texto = input(mensagem)
            try:
                return datetime.strptime(texto, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa, por exemplo 17/05/2000.")