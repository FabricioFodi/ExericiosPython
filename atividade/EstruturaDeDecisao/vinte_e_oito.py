# Exercício 28
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no
# cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.
import os


def valida_escolha(tipo_carne_str):
    if not tipo_carne_str.isdigit() or int(tipo_carne_str) not in {1, 2, 3}:
        raise ValueError('Valor inválido. Informe um dos valores sugeridos.')
    return int(tipo_carne_str)


def valida_quantidade(quantidade_str):
    try:
        quantidade = float(quantidade_str)
        if quantidade <= 0:
            raise ValueError('A quantidade deve ser maior que zero.')
    except ValueError:
        raise ValueError('Quantidade inválida. Informe um número válido.')
    return quantidade


table_md = """
|               | Até 5 Kg           | Acima de 5 Kg    |
|---------------|--------------------|------------------|
| File Duplo    | R$ 4,90 por Kg     | R$ 5,80 por Kg   |
| Alcatra       | R$ 5,90 por Kg     | R$ 6,80 por Kg   |
| Picanha       | R$ 6,90 por Kg     | R$ 7,80 por Kg   |
"""
print(table_md)

# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"

fileDuplo = 4.90
fileDuplo5kg = 5.80
alcatra = 5.90
alcatra5kg = 6.80
picanha = 6.90
picanha5kg = 7.80

while True:
    try:
        tipo_carne_str = input('Escolha apenas um tipo de carne\n1 - File Duplo\n2 - Alcatra\n3 - Picanha\nR: ')
        tipo_carne = valida_escolha(tipo_carne_str)

        quantidade_str = input('Informe a quantidade(kg): ')
        quantidade = valida_quantidade(quantidade_str)

        if tipo_carne == 1:
            if quantidade > 5:
                preco = fileDuplo5kg
            else:
                preco = fileDuplo
            total = preco * quantidade
            print(f'Total: R${total:.2f}')

        elif tipo_carne == 2:
            if quantidade > 5:
                preco = alcatra5kg
            else:
                preco = alcatra
            total = preco * quantidade
            print(f'Total: R${total:.2f}')

        elif tipo_carne == 3:
            if quantidade > 5:
                preco = picanha5kg
            else:
                preco = picanha
            total = preco * quantidade
            print(f'Total: R${total:.2f}')
        break
    except ValueError as ve:
        print(f'{RED}Erro: {ve}{RESET}\n') # exibe o erro em vermelho para melhor destaque
    except KeyboardInterrupt:
        print('\nOpreação interrompida pelo usuário.')
        break
