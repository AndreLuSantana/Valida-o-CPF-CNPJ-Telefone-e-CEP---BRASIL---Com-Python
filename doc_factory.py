from cpf import DocCpf
from cnpj import DocCnpj


class DocFactory:

    @staticmethod
    def create_doc(doc):
        if len(str(doc)) == 11:
            return DocCpf(doc)
        elif len(str(doc)) == 14:
            return DocCnpj(doc)
        else:
            raise ValueError('Quantidade de dígitos inválida.')
