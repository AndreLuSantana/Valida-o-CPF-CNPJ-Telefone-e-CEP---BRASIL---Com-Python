from validate_docbr import CNPJ


class DocCnpj:

    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.doc = documento
        else:
            raise ValueError('Número CNPJ inválido!!!')

    def __str__(self):
        return self.format_doc()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format_doc(self):
        formatador = CNPJ()
        return formatador.mask(self.doc)
