# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
consoante = 0
vogal = 0

for i in range(10):
    caracter = input(f'Digite o {i + 1}º caracter: ').lower()
    vetor.append(caracter)
    if caracter not in ['a', 'e', 'i', 'o', 'u'] and caracter.isalpha():
        consoante += 1
    else:
        vogal += 1
print(f'Total de Consoantes: {consoante}')
print(f'Total de Vogals: {vogal}')
