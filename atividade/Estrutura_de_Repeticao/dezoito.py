# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

def validaNum(n_str):
    if not n_str.isdigit():
        raise ValueError('Informe um valor válido.')
    return int(n_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            while True:
                try:
                    lista = []
                    n_str = input('Informe quantos números deseja: ')
                    n = validaNum(n_str)
                    break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')
            while True:
                try:
                    for i in range(n):
                        n_str = input(f'Informe o {i + 1}° número:')
                        m = validaNum(n_str)
                        lista.append(m)
                    break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')

            maior_numero = lista[0]
            menor_numero = lista[0]
            soma = 0

            for numero in lista:
                if numero > maior_numero:
                    maior_numero = numero
                if numero < menor_numero:
                    menor_numero = numero
                soma += numero

            print(f'O maior número é {maior_numero}')
            print(f'O menor número é: {menor_numero}')
            print(f'A soma dos números é: {soma}')
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
