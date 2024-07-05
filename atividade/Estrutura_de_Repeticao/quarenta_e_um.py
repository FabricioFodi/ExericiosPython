# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


def calcula_aumento(valor_da_divida, parcelas_iniciais, juros_inicial):
    valor_atual = valor_da_divida
    parcelas_atuais = parcelas_iniciais
    juros_atuais = juros_inicial

    print('Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela')

    for i in range(5):  # Executar 5 vezes conforme a tabela fornecida
        valor_juros = valor_atual - valor_da_divida
        valor_parcela = valor_atual / parcelas_atuais
        print(
            f'R${valor_atual:.2f}        R${valor_juros:.2f}            {parcelas_atuais}                    R${valor_parcela:.2f}')

        juros_atuais *= 2
        if parcelas_atuais == 1:
            parcelas_atuais = 3
        else:
            parcelas_atuais += 3

        valor_atual = valor_da_divida * (1 + juros_atuais / 100)


valor_da_divida = float(input('Digite o valor da dívida: '))
parcelas_iniciais = 1
juros_inicial = 1

calcula_aumento(valor_da_divida, parcelas_iniciais, juros_inicial)
