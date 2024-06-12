# Exercício 26
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

def valida_entrada(escolha):
    if escolha not in {'a', 'A', 'g', 'G'}:
        raise ValueError('Valor Inválido. Insira apenas "A" ou "G"')

    return escolha


def valida_valor(valor_str):
    if not valor_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor Inválido. Insira apenas números')

    valor = float(valor_str)

    return valor


preco_gasolina = 2.50
preco_alcool = 1.90

while True:
    try:
        escolha = input('Qual Combustivel o senhor vai querer?\nA - Álcool\nG - Gasolina\nR:')
        escolha = valida_entrada(escolha)
        valor_str = input(f'Quanto de {"Álcool" if escolha == 'A' else "Gasolina"} o senhor vai querer? ')
        valor = valida_valor(valor_str)

        if escolha == 'A':
            total = valor / preco_alcool
            if total <= 20:
                desconto = total * 0.03
                valor_com_desconto = total - desconto
                novo_valor = valor_com_desconto * preco_alcool
                print(f'{total:.1f} litros')
                print(f'Desconto {desconto:.1f}')
                print(f'Com desconto R${novo_valor:.2f}')
            else:
                desconto = total * 0.05
                valor_com_desconto = total - desconto
                novo_valor = valor_com_desconto * preco_alcool
                print(f'{total:.1f} l')
                print(f'Desconto {desconto:.1f} l ')
                print(f'Com desconto R${novo_valor:.2f}')
        else:
            total = valor / preco_gasolina
            if total <= 20:
                desconto = total * 0.04
                valor_com_desconto = total - desconto
                novo_valor = valor_com_desconto * preco_gasolina
                print(f'{total:.1f} litros')
                print(f'Desconto {desconto:.1f} litro{"s"if desconto >1 else ""}')
                print(f'Com desconto R${novo_valor:.2f}')
            else:
                desconto = total * 0.06
                valor_com_desconto = total - desconto
                novo_valor = valor_com_desconto * preco_gasolina
                print(f'{total:.1f} litros')
                print(f'Desconto {desconto:.1f} litro{"s"if desconto >1 else ""} ')
                print(f'Com desconto R${novo_valor:.2f}')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário')
        break