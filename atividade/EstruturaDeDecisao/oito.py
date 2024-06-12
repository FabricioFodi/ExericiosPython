# Exercício 8
# Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

def valida_preco(preco_str):
    if not preco_str.replace('.', '', 2).isdigit():
        raise TypeError('Digite apenas números.')

    preco = float(preco_str)

    return preco

while True:
    try:
        preco1_str = input('Informe o preço do primeiro produto: ')
        preco1 = valida_preco(preco1_str)

        preco2_str = input('Informe o preço do segundo produto: ')
        preco2 = valida_preco(preco2_str)

        preco3_str = input('Informe o preço do terceiro produto: ')
        preco3 = valida_preco(preco3_str)

        if preco1 == preco2 == preco3:
            print('Os preços são iguais.')
        else:
            menor = min(preco1, preco2, preco3)

            print(f'O produto com preço mais baixo é R${menor} ')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário')
        break