# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []
alunos = 10

for i in range(alunos):
    altura = float(input(f'Altura do {i + 1}° aluno: '))
    idade = int(input(f'Idade do {i + 1}° aluno: '))
    alturas.append(altura)
    idades.append(idade)

media = sum(alturas) / len(alturas)
print(f'Média da turma: {media:.2f}')

alunos_abaixo_media = len([i for i in range(alunos) if idades[i] > 13 and alturas[i] < media])

print(f'Número de alunos com mais de 13 anos e altura inferior à média: {alunos_abaixo_media}')
