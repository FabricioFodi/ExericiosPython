# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorA = []
vetorB = []
vetorC = []
total = 5

print('Informe 5 números para o primeiro vetor.')
for i in range(total):
    numeros = int(input(f'Informe o {i + 1}º número: '))
    vetorA.append(numeros)

print('Informe 5 números para o segundo vetor.')

for i in range(total):
    numeros = int(input(f'Infome o {i + 1}º número: '))
    vetorB.append(numeros)

for i in range(total):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])

print(vetorA)
print(vetorB)
print(vetorC)