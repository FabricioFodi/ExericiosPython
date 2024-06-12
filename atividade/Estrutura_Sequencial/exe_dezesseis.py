# Exercício 16
# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

cobertura_por_litro = 3 # metros quadrados por litro
capacidade_lata = 18
valor = 80.0

areaSerPintada = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

# Calcula quantos litros serão necessários dividindo o input por 3.
litros_necessarios = areaSerPintada / cobertura_por_litro

#Calcula o número de latas de tinta necessárias. A função math.ceil é usada para arredondar
# para cima, garantindo que mesmo uma pequena fração de lata seja contada como uma lata inteira,
# já que não se pode comprar uma fração de lata.
latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)

#Calcula o custo total multiplicando o número de latas pelo preço de cada lata.
custo_total = latas_necessarias * valor

print(f"Quantidade de latas de tinta a serem compradas: {latas_necessarias}")
print(f"Preço total: R$ {custo_total:.2f}")