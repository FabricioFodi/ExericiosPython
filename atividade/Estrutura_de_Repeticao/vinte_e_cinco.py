# Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60
# e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
import time


def calcula_media(pessoas):
    soma = sum(pessoas)
    media = soma / len(pessoas)
    return media


pessoas = []
quantidade = int(input('Quantas pessoas tem na sala? '))

for i in range(quantidade):
    idade = int(input(f'Digite a idade da {i + 1}ª pessoa: '))
    pessoas.append(idade)

print("Idades registradas.")
time.sleep(1)
print('Calculando.')
time.sleep(1)
print('Calculando..')
time.sleep(1)
print('Calculando...')
time.sleep(1)

media = calcula_media(pessoas)
if idade <= 25:
    print('Turma jovem')
elif 26 <= idade <= 60:
    print('Turma Adulta')
else:
    print('Turma Idosa')
