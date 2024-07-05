# Altere o programa de cálculo dos números primos,
# informando, caso o número não seja primo, por quais número ele é divisível.

def validaNumero(numero_str):
    if not numero_str.isdigit():
        raise ValueError("Numero invalido")
    return int(numero_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            numero_str = input('informe um número: ')
            numero = validaNumero(numero_str)
            ehPrimo = True
            divisores = []

            if numero < 2:
                ehPrimo = False

            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    ehPrimo = False
                    divisores.append(i)
                    if i != numero // i:
                        divisores.append(numero // i)

            if ehPrimo and numero > 1:
                print(f'{numero} é primo ')
            else:
                print(f'{numero} não é primo. Ele é divisível por: {sorted(divisores)}')
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
