# Exercício 15
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 1. salário bruto.
# 2. quanto pagou ao INSS.
# 3. quanto pagou ao sindicato.
# 4. o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input('Quanto você ganha por hora? '))
hrTrab = int(input('Quantas horas você trabalha no mês? '))

salario = hora * hrTrab
inss = (salario / 100) * 8
ir = (salario / 100) * 11
sindicato = (salario / 100) * 5
desconto = inss + ir + sindicato
sal_liquido = salario - desconto

print(f"Você ganha bruto por mês: {salario:.2f} R$")
print(f"você ganha liquido por mes: {sal_liquido:.2f} R$")
print(f"Desconto do INSS: {inss} R$")
print(f"Desconto do Imposto de Renda: {ir} R$")
print(f"Desconto do Sindicato: {sindicato} R$")
print(f"Soma dos descontos: {desconto} R$")