# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.

def validaNumero(numero_str):
    if not numero_str.isdigit():
        raise ValueError('Informe um número inteiro')
    return int(numero_str)


RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            numero1_str = input('Informe um número: ')
            numero1 = validaNumero(numero1_str)
            numero2_str = input('Informe outro número: ')
            numero2 = validaNumero(numero2_str)

            if numero1 > numero2:
                numero1, numero2 = numero2, numero1

            print(f"Números no intervalo entre {numero1} e {numero2}:")

            for i in range(numero1 + 1, numero2):
                print(i)
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
