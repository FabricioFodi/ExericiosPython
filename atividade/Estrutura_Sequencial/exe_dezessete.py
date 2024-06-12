# Exercício 17
# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1. comprar apenas latas de 18 litros;
# 2. comprar apenas galões de 3,6 litros;
# 3. misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# Definindo os preços e capacidades
valor_lata = 80.0
valor_galao = 25.0
cobertura_por_litro = 6
capacidade_lata = 18
capacidade_galao = 3.6

# Solicitando a área a ser pintada
area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

# Acrescentando 10% de folga
area_com_folga = area * 1.10

# Calculando a quantidade total de tinta necessária (em litros)
litros_necessarios = area_com_folga / cobertura_por_litro

# Situação 1: Comprar apenas latas de 18 litros
latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)
custo_latas = latas_necessarias * valor_lata

# Situação 2: Comprar apenas galões de 3,6 litros
galoes_necessarios = math.ceil(litros_necessarios / capacidade_galao)
custo_galoes = galoes_necessarios * valor_galao

# Situação 3: Misturar latas e galões para minimizar desperdício
# "math.floor" Calcula o número de latas necessárias arredondando para baixo para deixar o mínimo restante.
latas_necessarias_mix = math.floor(litros_necessarios / capacidade_lata)
resto_litros = litros_necessarios - (latas_necessarias_mix * capacidade_lata)
galoes_necessarios_mix = math.ceil(resto_litros / capacidade_galao)
custo_mix = (latas_necessarias_mix * valor_lata) + (galoes_necessarios_mix * valor_galao)


print(f"\nPara pintar {area:.2f} metros quadrados (com folga de 10%):")
print(f"1. Comprando apenas latas de 18 litros:")
print(f"   - Latas necessárias: {latas_necessarias}")
print(f"   - Custo: R$ {custo_latas:.2f}")

print(f"2. Comprando apenas galões de 3,6 litros:")
print(f"   - Galões necessários: {galoes_necessarios}")
print(f"   - Custo: R$ {custo_galoes:.2f}")

print(f"3. Misturando latas e galões para menor desperdício:")
print(f"   - Latas necessárias: {latas_necessarias_mix}")
print(f"   - Galões necessários: {galoes_necessarios_mix}")
print(f"   - Custo: R$ {custo_mix:.2f}")

