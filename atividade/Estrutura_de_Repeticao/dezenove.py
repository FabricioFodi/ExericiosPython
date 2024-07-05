# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

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
            lista = []
            while True:
                try:
                    n_str = input('Informe quantos números deseja: ')
                    n = validaNum(n_str)
                    if n > 1000 or n < 0:
                        print('informe um número menor q 1000.')
                    else:
                        break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')
            i = 0
            while i < n:
                n_str = input(f'Informe o {i + 1}° número: ')
                try:
                    m = validaNum(n_str)
                    if m > 1000 or m < 0:
                        print('Informe um número maior que 0 e menor que 1000.')
                    else:
                        lista.append(m)
                        i += 1  # Incrementa apenas se a entrada for válida
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
