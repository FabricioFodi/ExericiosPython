# Exercício 15
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes;

def valida_triangulo(lado_str):
    if not lado_str.isdigit():
        raise ValueError('Digite um valor válido')

    lado = int(lado_str)

    return lado


while True:
    try:
        lado1_str = int(input('Digite o lado 1: '))
        lado2_str = int(input('Digite o lado 2: '))
        lado3_str = int(input('Digite o lado 3: '))
        if lado1_str + lado2_str > lado3_str or lado1_str + lado3_str > lado2_str or lado2_str + lado3_str > lado1_str:
            if lado1_str == lado2_str == lado3_str:
                print('Triângulo Equilátero')
            elif lado1_str == lado2_str or lado1_str == lado3_str or lado2_str == lado3_str:
                print('Triângulo Isóceles')
            else:
                print('Triângulo Escaleno')
        else:
            print('isto não é um triângulo')
        break
    except ValueError as ve:
        print(f'Erro 401: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompido pelo usuário.')