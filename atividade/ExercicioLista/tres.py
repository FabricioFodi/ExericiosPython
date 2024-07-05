# Faça um Programa que leia 4 notas, mostre as notas e a média na tela

def valida_nota(nota_str):
    if not nota_str.replace('.', '', 1).isdigit():
        raise ValueError('Nota inválida')
    nota = float(nota_str)
    if nota < 0 or nota > 10:
        raise ValueError('Nota inválida.')
    return nota


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    notas = []
    while True:
        try:
            for i in range(4):
                nota_str = input(f'Informe a {i + 1}ª nota: ')
                nota = valida_nota(nota_str)
                notas.append(nota)
            media = sum(notas) / 4
            print(f'Média final: {media:.2f}')
            if media >= 7:
                print('Aprovado :)')
            else:
                print('Reprovado ;(')
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