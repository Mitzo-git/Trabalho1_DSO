class TipoAtendimentoJaCadastradoException(Exception):
    def __init__(self):
        super().__init__("Já existe um tipo de atendimento com esse nome")