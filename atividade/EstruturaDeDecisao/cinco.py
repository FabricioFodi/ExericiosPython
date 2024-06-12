# Exercício 5
# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def valida_nota(nota_str):
    if not nota_str.replace('.', '', 1).isdigit():
        raise TypeError('Digite apenas números.')

    nota = float(nota_str)

    if nota < 0 or nota > 10:
        raise ValueError('Nota invalida.')

    return nota


while True:
    try:
        nota1_str = input('Digite a primeira nota: ')
        nota1 = valida_nota(nota1_str)

        nota2_str = input('Digite a segunda nota: ')
        nota2 = valida_nota(nota2_str)

        media = (nota1 + nota2) / 2

        if media == 10:
            print('Aprovado com Distinção!')
        elif media >= 7:
            print('Aprovado!')
        else:
            print('Reprovado!')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        break
