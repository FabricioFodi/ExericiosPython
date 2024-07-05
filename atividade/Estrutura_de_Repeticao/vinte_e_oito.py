# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

def validaCD(cds_str):
    if not cds_str.isdigit():
        raise ValueError('Valor inválido.')
    return int(cds_str)


def validaPreco(preco_str):
    if not preco_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor inválido')
    return float(preco_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:

            cds_str = input('Digite a quantidade de CDS comprados: ')
            cds = validaCD(cds_str)

            total_preco_cds = 0

            for i in range(1, cds + 1):
                while True:
                    try:
                        preco_str = input(f'Informe o valor do {i}º CD: ')
                        preco = validaPreco(preco_str)
                        total_preco_cds += preco
                        break
                    except ValueError as ve:
                        print(f'{RED}Erro: {ve}{RESET}\n')

            try:
                media_preco = total_preco_cds / cds
                print(f'O valor total investido: R${total_preco_cds:.2f}')
                print(f'A média de preço por CD é: R${media_preco:.2f}')
            except ZeroDivisionError:
                print(f'{RED}Esta entrada não é permitida.'
                      f'\n Erro: Divisão por zero não permitida.{RESET}')
                break

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
