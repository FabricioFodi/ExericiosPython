# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor_par = []
vetor_impar = []
vetor = []

for i in range(10):
    numeros = int(input(f'Informe o {i + 1}º número: '))
    vetor.append(numeros)
    if numeros % 2 == 0:
        vetor_par.append(numeros)
    else:
        vetor_impar.append(numeros)
print(f'Todos os números: {vetor}')
print(f'Apenas números pares: {vetor_par}')
print(f'Apenas números impares: {vetor_impar}')