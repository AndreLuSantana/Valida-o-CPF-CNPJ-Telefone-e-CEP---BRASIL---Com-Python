from datetime import datetime, timedelta

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
            'agosto',  'setembro', 'outubro', 'novembro', 'dezembro'
        ]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def dia_semana(self):
        dias_da_semana = [
            'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira',
            'sábado', 'domingo'
        ]
        dia = self.momento_cadastro.weekday()
        return dias_da_semana[dia]

    def data_formatada(self):
        return self.momento_cadastro.strftime('%d/%m/%Y')

    def data_formatada_com_hora(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def tempo_de_cadastro(self):
        return datetime.today() - self.momento_cadastro
