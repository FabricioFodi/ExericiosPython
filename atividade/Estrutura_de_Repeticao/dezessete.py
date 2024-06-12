# Faça um programa que calcule o fatorial de um número
# inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def validaNum(n_str):
    if not n_str.isdigit():
        raise ValueError('Informe um número válido')
    return int(n_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    n_str = input('Informe um número fatorial: ')
    n = validaNum(n_str)

    count = 0
    fatorial = 1
    while True:
        try:
            for i in range(1, n + 1):
                fatorial *= i
            print(f'Fatorial de {i} é {fatorial}')
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
