# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
# e limitando o fatorial a números inteiros positivos e menores que 16.

def validaNum(n_str):
    if not n_str.isdigit():
        raise ValueError('Informe apenas dígitos.')
    return int(n_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            count = 0
            fatorial = 1
            n = int(input('Informe um número fatorial: '))
            if n > 16 or n < 1:
                raise ValueError('Informe apenas números inteiros.')
            else:
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
