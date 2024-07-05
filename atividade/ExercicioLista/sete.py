# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
multi = 1
for i in range(5):
    numero = int(input(f'Informe o {i + 1}º número: '))
    numeros.append(numero)
soma = sum(numeros)
for valor in numeros:
    multi *= valor
print(f'Soma: {soma}')
print(f'Multiplicação: {multi}')
print(f'números: {numeros}')