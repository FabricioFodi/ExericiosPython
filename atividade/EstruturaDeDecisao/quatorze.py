# Exercício 14
# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def valida_notas(notas_str):
    if not notas_str.replace('.', '', 1).isdigit():
        raise ValueError('Digite um valor válido.')

    nota = float(notas_str)

    if nota < 0 or nota > 10:
        raise ValueError('A nota deve estar entre 0 e 10.')

    return nota

while True:
    try:
        nota1_str = input('Digite Uma nota: ')
        nota1 = valida_notas(nota1_str)
        nota2_str = input('Digite Uma nota: ')
        nota2 = valida_notas(nota2_str)
        media = (nota1 + nota2) / 2
        if 9 < media <= 10:
            print(f'Notas: {nota1_str} - {nota2_str}\nMédia: {media}')
            print('nota "A"!\nAprovado!')
        elif 7.5 < media <= 9:
            print(f'Notas: {nota1_str} - {nota2_str}\nMédia: {media}')
            print('nota "B"!\nAprovado!')
        elif 6 < media <= 7.5:
            print(f'Notas: {nota1_str} - {nota2_str}\nMédia: {media}')
            print('nota "C"!\nAprovado')
        elif 4 < media <= 6:
            print(f'Notas: {nota1_str} - {nota2_str}\nMédia: {media}')
            print('nota "D"!\nReprovado')
        else:
            print(f'Notas: {nota1_str} - {nota2_str}\nMédia: {media}')
            print('nota "F"!\nReprovado!')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('\nOpração interrompida pelo usuário.')
        break