# Exercício 11
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# 1. salários até R$ 280,00 (incluindo) : aumento de 20%
# 2. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# 3. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# 4. salários de R$ 1500,00 em diante : aumento de 5%
#   Após o aumento ser realizado, informe na tela:
# 1. o salário antes do reajuste;
# 2. o percentual de aumento aplicado;
# 3. o valor do aumento;
# 4. o novo salário, após o aumento.

def valida_salario(salario_str):
    try:
        salario = float(salario_str)  # Converter para float
    except ValueError:
        raise ValueError('Digite um número válido.')

    if salario <= 99:
        raise ValueError('O salário não pode ser abaixo de 100.')

    return salario

while True:
    try:
        salario_str = input('Informe seu Salário: ')
        salario = valida_salario(salario_str)

        if salario <= 280.00:
            percentual = 20
        elif salario <= 700.00:
            percentual = 15
        elif salario <= 1500.00:
            percentual = 10
        else:
            percentual = 5

        reajuste = salario * percentual / 100
        novo_salario = salario + reajuste
        print(f'Salário antes do reajuste: R${salario:.2f}')
        print(f'Reajuste de {percentual}%')
        print(f'Valor do reajuste: R${reajuste:.2f}')
        print(f'Seu novo salário é de R${novo_salario:.2f}')

        break
    except ValueError as ve:
        print(f'Erro {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break
