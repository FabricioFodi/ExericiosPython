# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.
import sys


def valida_entrada(entrada_str):
    if entrada_str == "":
        print(f'{RED}Encerrando programa{RESET}')
        sys.exit()
    if entrada_str not in ['100', '101', '102', '103', '104', '105']:
        raise ValueError('Valor Inválido')
    return int(entrada_str)


def valida_quantidade(quantidade_str):
    if quantidade_str == "":
        print(f'{RED}Encerrando programa{RESET}')
        sys.exit()
    if not quantidade_str.isnumeric():
        raise ValueError('Valor Inválido')
    return int(quantidade_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"

hotdog = 1.20
bauru_simples = 1.30
bauru_com_ovo = 1.50
burguer = 1.20
Chesseburguer = 1.30
refri = 1


def main():
    while True:
        try:
            print(f"{'Especificação':<16} {'Código':<7} {'Preço':<6}")
            print(f"{'Cachorro Quente':<16} {'100':<7} {'R$ 1,20':<6}")
            print(f"{'Bauru Simples':<16} {'101':<7} {'R$ 1,30':<6}")
            print(f"{'Bauru com ovo':<16} {'102':<7} {'R$ 1,50':<6}")
            print(f"{'Hambúrguer':<16} {'103':<7} {'R$ 1,20':<6}")
            print(f"{'Cheeseburguer':<16} {'104':<7} {'R$ 1,30':<6}")
            print(f"{'Refrigerante':<16} {'105':<7} {'R$ 1,00':<6}")

            entrada1_str = input("\nInforme o código do produto: ")
            escolha = valida_entrada(entrada1_str)

            quantidade_str = input("Informe a quantidade de produtos: ")
            quantidade = valida_entrada(quantidade_str)

            if escolha == 100:
                preco = hotdog * quantidade
            elif escolha == 101:
                preco = bauru_simples * quantidade
            elif escolha == 102:
                preco = bauru_com_ovo * quantidade
            elif escolha == 103:
                preco = burguer * quantidade
            elif escolha == 104:
                preco = Chesseburguer * quantidade
            elif escolha == 105:
                preco = Chesseburguer * quantidade

            print(f'Total a pagar: R${preco:.2f}')
            dinheiro = float(input("Informe o valor em dinheiro: "))
            troco = dinheiro - preco
            if dinheiro < preco:
                print(f'Faltando dinheiro')
            else:
                print(f'Seu troco: R${troco:.2f}')
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
