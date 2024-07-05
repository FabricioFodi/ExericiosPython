# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

medias = []
notas_por_aluno = 4
total_alunos = 3
for aluno in range(total_alunos):
    notas = []
    for i in range(notas_por_aluno):
        while True:
            nota = float(input(f'Digite {i + 1}ª nota: '))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print('Nota inválida. Digite uma nota entre 0 e 10.')
    media = sum(notas) / len(notas)
    medias.append(media)
    print(f'Média do {aluno + 1}º aluno: {media:.2f}')

aluno_maior_que_sete = len([media for media in medias if media >= 7])
print(f'O número de alunos que tem média acima de 7: {aluno_maior_que_sete}')
