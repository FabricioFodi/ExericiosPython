# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120


def valida_entrada(n_str):
    if not n_str.isdigit():
        raise ValueError('Valor inválido.')
    return int(n_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            n_str = input('Informe o valor a ser fatorado: ')
            n = valida_entrada(n_str)

            fatorial = 1
            resultado = f'{n}! = '
            for i in range(1, n + 1):
                fatorial *= i
                resultado += f' {i} .'
            resultado = resultado[:-2] + f' = {fatorial}'  # Removendo o último " ."
            print(resultado)
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
