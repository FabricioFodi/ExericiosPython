# Exercício 27
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def valida_compra(comprarMaca_str, comprarMorango_str):
    comprarMorango = float(comprarMorango_str)
    comprarMaca = float(comprarMaca_str)

    if not comprarMaca_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor Inválido.')

    if not comprarMorango_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor Inválido.')

    return comprarMorango, comprarMaca


tabela_md = """
|         | Até 5 Kg         | Acima de 5 Kg    |
|---------|------------------|------------------|
| Morango | R$ 2,50 por Kg   | R$ 2,20 por Kg   |
| Maçã    | R$ 1,80 por Kg   | R$ 1,50 por Kg   |
"""
print(tabela_md)

morango = 2.50
maca = 1.80
morango5kg = 2.20
maca5kg = 1.50

while True:
    try:
        comprarMaca_str = input('Informe a quantidade de maça(kg): ')
        comprarMorango_str = input('Informe a quantidade de morango(kg): ')

        comprarMorango, comprarMaca = valida_compra(comprarMaca_str, comprarMorango_str)

        if comprarMaca > 5:
            total1 = comprarMaca * maca5kg
            print(f'Valor com desconto acima de 5kg maçãs: R${total1:.2f}')
        else:
            preco = maca
            total1 = comprarMaca * preco
            print(f'Valor da compra das maçãs: R${total1:.2f}')

        if comprarMorango > 5:
            total = comprarMorango * morango5kg
            print(f'Valor com desconto acima de 5kg morangos: R${total:.2f}')
        else:
            preco = morango
            total = comprarMorango * preco
            print(f'Valor da compra dos morangos: R${total:.2f}')

        soma = total1 + total
        print(f'Total: R${soma}')

        if soma > 25:
            desconto = (10 / 100) * soma
            soma_com_desconto = soma - desconto
            print(f'Total: R${soma_com_desconto:.2f}(10% desconto)')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário.')
        break