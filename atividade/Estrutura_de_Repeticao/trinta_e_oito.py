# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto,
# altere o programa permitindo que o usuário digite o salário inicial do funcionário.

import datetime


def calcula_aumento_anual(salario_inicial, ano_inicial, ano_atual, aumento_inicial):
    salario_atual = salario_inicial
    aumento_anual = aumento_inicial

    for ano in range(ano_inicial, ano_atual + 1):
        print(f"Ano: {ano} - Salário: R${salario_atual:.2f} - Aumento anual: {aumento_anual:.2f}%")
        if ano < ano_atual:
            salario_atual *= (1 + aumento_anual / 100)
            aumento_anual *= 2


# Configurações iniciais
salario_inicial = 1000.00
# Obter o ano atual
ano_atual = datetime.datetime.now().year
# Definir o ano inicial
ano_inicial = 1996
aumento_inicial = 1.5

calcula_aumento_anual(salario_inicial, ano_inicial, ano_atual, aumento_inicial)
