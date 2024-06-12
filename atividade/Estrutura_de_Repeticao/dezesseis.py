# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

def validaNum(fn_str):
    if not fn_str.isdigit():
        raise ValueError('Informe um número inteiro positivo.')
    return int(fn_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            f1, f2 = 0, 1
            fn_str = input('Informe o número que deseja: ')
            fn = validaNum(fn_str)

            if fn < 500:
                print('O valor da série precisa ser maior que 500.')
            else:
                for i in range(fn):  # "i" == quantidade de iterações "n" == input
                    while f1 <= fn:
                        print(f1, end=' ')
                        f1, f2 = f2, f1 + f2
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit


while True:
    try:
        main()
        resposta = input(f'\n{BROWN}Quer continuar? [S/N]{RESET}: ')
        if resposta.lower() != 's':
            print(f'{BROWN}Programa finalizado.{RESET}')
            break
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
