# Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.

def valida_entrada(num_str):
    if not num_str.replace('-', '', 1).isdigit():
        raise ValueError ('Informe um valor inteiro')
    return int(num_str)


numeros = []

intervalos = {
    '0-25': [],
    '26-50': [],
    '51-75': [],
    '76-100': [],
}
# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:

            while True:
                try:
                    num_str = input('Informe um número inteiro (números negativos encerrarão a aplicação): ')
                    num = valida_entrada(num_str)

                    if num < 0:
                        break
                    numeros.append(num)
                    if 0 <= num <= 25:
                        intervalos['0-25'].append(num)
                    elif 25 <= num <= 50:
                        intervalos['26-50'].append(num)
                    elif 50 <= num <= 75:
                        intervalos['51-75'].append(num)
                    elif 75 <= num <= 100:
                        intervalos['76-100'].append(num)
                        break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')

            for intervalo, nums in intervalos.items():
                print(f'{intervalo}: {nums}')
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