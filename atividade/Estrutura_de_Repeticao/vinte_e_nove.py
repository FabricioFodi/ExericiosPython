# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que
# contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma
# a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
# Você foi contratado para desenvolver o programa que monta esta tabela de preços,
# que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

def valida_itens(itens_str):
    if not itens_str.isdigit():
        raise ValueError('Valor inválido.')
    itens = int(itens_str)

    if itens < 1 or itens > 50:
        raise ValueError('A quantidade deve estar entre 1 e 50')

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

            preco = 1.99
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
