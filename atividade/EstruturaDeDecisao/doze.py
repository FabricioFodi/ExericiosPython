# Exercício 12
# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

def valida_horas(hora_str, horaTrabalhada_str):
    if hora_str <= 0 or horaTrabalhada_str <= 0:
        raise ValueError('Hora invalida')

    hora = int(hora_str)
    horaTrabalhada = int(horaTrabalhada_str)

    return hora, horaTrabalhada


while True:
    try:
        hora_str = float(input('Informe o valor da sua hora: '))
        hora = valida_horas(hora_str, hora_str)
        horaTrabalhada_str = int(input('Informe quantas horas você trabalha no mês: '))
        horaTrabalhada = valida_horas(horaTrabalhada_str, horaTrabalhada_str)

        salario = hora_str * horaTrabalhada_str


        if salario <= 900:
            desconto_ir = 0
        elif salario <=1500:
            desconto_ir = 5
        elif salario <=2500:
            desconto_ir = 10
        else:
            desconto_ir = 20

        reajuste = (salario * desconto_ir) / 100
        reajuste_inss = (salario * 10) / 100
        reajuste_fgts = (salario * 11) / 100
        total_desconto = reajuste_inss + reajuste
        salario_liquido = salario - total_desconto


        print(f'        Salário Bruto: ({hora_str:.2f} * {horaTrabalhada_str})        : R$ {salario:.2f}')
        print(f'        (-) IR ({desconto_ir}%)                     : R$ {reajuste:.2f}')
        print(f'        (-) INSS (10%)                 : R$ {reajuste_inss:.2f}')
        print(f'        FGTS (11%)                      : R$ {reajuste_fgts:.2f}')
        print(f'        Total de descontos              : R$ {total_desconto:.2f}')
        print(f'        Salário Líquido                 : R$ {salario_liquido:.2f}')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break

