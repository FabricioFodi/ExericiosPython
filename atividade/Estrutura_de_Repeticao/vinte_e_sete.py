# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos

def validaTurma(turmas_str):
    if not turmas_str.isdigit():
        raise ValueError('Valor inválido.')
    return int(turmas_str)


def validaAlunos(alunos_str):
    if not alunos_str.isdigit():
        raise ValueError('Valor inválido.')

    alunos = int(alunos_str)

    if 0 <= alunos > 40:
        raise ValueError('Valor inválido.')

    return alunos


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            turmas_str = input('Turmas: ')
            turmas = validaTurma(turmas_str)

            total_alunos = 0

            for i in range(1, turmas + 1):
                while True:
                    try:
                        alunos_str = input(f'Alunos na turma {i}: ')
                        alunos = validaAlunos(alunos_str)
                        total_alunos += alunos
                        break
                    except ValueError as ve:
                        print(f'{RED}Erro: {ve}{RESET}\n')
            media = total_alunos // turmas

            print(f'A média de alunos de {turmas} turmas é de {media} por sala.')
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit


while True:
    try:
        main()
        resposta = input(f'{BROWN}Quer continuar? [S/N]{RESET}: ')
        if resposta.lower() != 's':
            print(f'{BROWN}Programa finalizado.{RESET}')
            break
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
