# Exercício 16
# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
#       Se o usuário informar o valor de A igual a zero,
#   a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#       Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#       Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#       Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

# Função para calcular as raízes da equação do segundo grau
def validar_raizes(a, b, c):
    if a == 0:
        raise ValueError('A equação não é de segundo grau.')

    delta = b**2 - 4*a*c

    if delta < 0:
        raise ValueError('A equação não possui raízes reais.')

    return delta

while True:
    try:
        a = float(input('Informe o valor de a: '))
        validar_raizes(a, 0, 0)  # Verifica se a é zero
        b = float(input('Informe o valor de b: '))
        c = float(input('Informe o valor de c: '))

        delta = validar_raizes(a, b, c)  # Verifica se a equação é válida

        if delta == 0:
            raiz = -b / (2*a)
            print(f"A equação possui uma raiz real: {raiz:.2f}")
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"A equação possui duas raízes reais:")
            print(f"Raiz 1: {raiz1:.2f}")
            print(f"Raiz 2: {raiz2:.2f}")

        break  # Encerra o loop após calcular as raízes

    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        break



