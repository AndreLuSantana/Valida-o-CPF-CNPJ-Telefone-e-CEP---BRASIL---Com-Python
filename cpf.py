from validate_docbr import CPF


class DocCpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.doc = documento
        else:
            raise ValueError('Número CPF inválido!!!')

    def __str__(self):
        return self.format_doc()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format_doc(self):
        formatador = CPF()
        return formatador.mask(self.doc)


