


class Carro:                               
    def __init__(self, cor, valor, ano):
        self.cor = cor
        self.valor = valor
        self.ano = ano

    def calcular_desconto(self, percentual_desconto):
        """Calcula o valor do carro com um determinado desconto.

        Args:
            percentual_desconto (float): Percentual de desconto a ser aplicado (entre 0 e 1).

        Returns:
            float: Valor do carro com o desconto aplicado.
        """

        desconto = self.valor * percentual_desconto
        valor_com_desconto = self.valor - desconto
        return valor_com_desconto

    def calcular_parcelamento(self, numero_parcelas):
        """Calcula o valor de cada parcela de um financiamento.

        Args:
            numero_parcelas (int): Número de parcelas do financiamento.

        Returns:
            float: Valor de cada parcela.
        """

        if numero_parcelas <= 0:
            raise ValueError("O número de parcelas deve ser maior que zero.")

        valor_parcela = self.valor / numero_parcelas
        return valor_parcela
