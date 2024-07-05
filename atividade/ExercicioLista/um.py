# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

def valida(numb_str):
    if not numb_str.replace('-', '', 1).isdigit():
        raise ValueError('Valor inválido')
    return int(numb_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    numeros = []
    for i in range(5):
        while True:
            try:
                numb_str = input(f'Infome {i + 1}° número: ')
                numb = valida(numb_str)
                numeros.append(numb)
                break
            except ValueError as ve:
                print(f'\n{RED}Erro: {RESET}')
            except KeyboardInterrupt:
                print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
                raise SystemExit

    print(f'Lista de números: {numeros}')


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


