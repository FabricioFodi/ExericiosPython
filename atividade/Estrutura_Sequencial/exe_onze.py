# Exercício 11
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

numero = int(input("informe um número: "))
numeroUm = int(input("informe outro número: "))
numeroReal = float(input("informe um número real: "))

calculoa = (numero * 2) * (numeroUm *0.5)
calculob = (numero * 3) + (numeroReal)
calculoc = numeroReal ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {calculoa:.1f}")
print(f"A soma do triplo do primeiro com o terceiro é: {calculob:.1f}")
print(f"O terceiro elevado ao cubo: {calculoc:.2f}")