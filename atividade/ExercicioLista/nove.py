# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = []
soma = 0
for i in range(5):
    numeros = int(input(f'Informe o {i + 1}º número: '))
    vetor.append(numeros)
for quadrado in vetor:
    potencia = pow(quadrado, 2)
    # print(f'{quadrado} = {potencia}')
    print(f'{quadrado}^2 = {pow(quadrado, 2)}')
    soma += potencia
print(f'Soma dos quadrados dos elementos do vetor : {soma}')


