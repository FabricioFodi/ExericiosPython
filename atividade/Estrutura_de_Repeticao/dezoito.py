# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
n = int(input('Informe quantos números deseja: '))

for i in range(n):
    m = int(input(f'Informe o {i +1}° número:'))
    lista.append(m)


maior_numero = lista[0]
menor_numero = lista[0]
soma = 0

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    soma += numero

print(f'O maior número é {maior_numero}')
print(f'O menor número é: {menor_numero}')
print(f'A soma dos números é: {soma}')

