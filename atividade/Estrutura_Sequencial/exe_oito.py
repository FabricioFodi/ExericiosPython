# Exercício 8
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto você ganha por hora? '))
hrTrab = int(input('Quantas horas você trabalha no mês? '))

calculo = hora * hrTrab

print(f"Você ganha por mês: {calculo:.2f} Reais")