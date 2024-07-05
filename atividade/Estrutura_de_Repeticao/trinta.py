# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta
# a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
# conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

def valida_itens(itens_str):
    if not itens_str.isdigit():
        raise ValueError ('Valor inválido.')

    itens = int(itens_str)

    if itens < 1 or itens > 50:
        raise ValueError ('A quantidade deve estar entre 1 e 50')

    return itens


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            itens_str = input('Informe quantos itens são: ')
            itens = valida_itens(itens_str)

            preco = 0.18
            total = 0
            for i in range(itens):
                total = preco * itens
            print(f'Total da compra: {total:.2f}')
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