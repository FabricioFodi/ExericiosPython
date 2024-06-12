# Exercício 24
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

def validar_numero(numero_str):
    if not numero_str.replace('.', '', 1).replace('-', '', 1).isdigit():
        raise ValueError("Valor invalido")

    numero = float(numero_str)
    return numero


while True:
    try:
        numero1_str = input('Informe um número: ')
        numero1 = validar_numero(numero1_str)
        numero2_str = input('Informe outro número: ')
        numero2 = validar_numero(numero2_str)

        escolha = input('Escolha uma das opções\n1 - Saber se os números são Inteiros ou Decimais\n2 - Saber se são positivo ou negativo\n3 - Saber se são impares ou pares\nR:')
        if escolha == '1':
            if numero1 == round(numero1) and numero2 == round(numero2):
                print(f'Os dois números são Inteiros')
            elif numero1 == round(numero1):
                print(f'Apenas o primeiro número é Inteiro.')
            elif numero2 != round(numero2) and numero1 != round(numero2):
                print('Os dois números são Decimais')
            else:
                print(f'Apenas o segundo número é Inteiro')

        if escolha == '2':
            if numero1 > 0 and numero2 > 0:
                print('Os números são positivos')
            elif numero1 < 0 and numero2 < 0:
                print('Os números são negativos')
            elif numero1 > 0 and numero2 < 0:
                print('O primeiro número é positivo e o segundo é negativo')
            elif numero1 < 0 and numero2 > 0:
                print('O primeiro número é negativo e o segundo número é positivo')
            elif numero1 < 0 and numero2 < 0:
                print('Os dois números são negativos')
            elif numero1 == 0 and numero2 < 0:
                print('O primeiro número é zero e o Segundo é negativo')
            elif numero1 < 0 and numero2 == 0:
                print('O primeiro número é negativo e o segundo é zero')
            elif numero1 == 0 and numero2 > 0:
                print('O primeiro número é zero e o segundo é positivo')
            elif numero1 > 0 and numero2 == 0:
                print('O primeiro número é positivo e o segundo é zero')
            else:
                print('Os dois números são zeros')

        if escolha == '3':
             if numero1 % 2 == 0 and numero2 % 2 == 0:
                 print('Os números são pares')
             elif numero1 % 2 == 0:
                print('O primeiro é par e o Segundo é impar')
             elif numero2 % 2 == 0:
                print('O primeiro é impar e o Segundo é par')
             else:
                print('Os dois números são impares')

        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break

# round inteiro ou decimal
# % 2 == 0 par ou impar
# positivo ou negativo