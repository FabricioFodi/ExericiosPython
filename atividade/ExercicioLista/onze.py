# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetorD = []
vetorE = []
vetorF = []
vetorG = []
total = 5

print('Informe 5 números para o primeiro vetor.')
for i in range(total):
    numeros = int(input(f'Informe o {i + 1}º número: '))
    vetorD.append(numeros)

print('Informe 5 números para o segundo vetor.')

for i in range(total):
    numeros = int(input(f'Infome o {i + 1}º número: '))
    vetorE.append(numeros)

print('Informe 5 números para o segundo vetor.')

for i in range(total):
    numeros = int(input(f'Infome o {i + 1}º número: '))
    vetorF.append(numeros)

for i in range(total):
    vetorG.append(vetorD[i])
    vetorG.append(vetorE[i])
    vetorG.append(vetorF[i])

print(vetorD)
print(vetorE)
print(vetorF)
print(vetorG)