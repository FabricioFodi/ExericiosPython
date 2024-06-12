# Ecercício 6
# Faça um Programa que leia três números e mostre o maior deles.

def valida_numero(numero_str):
    if not numero_str.isdigit():
        raise TypeError('Digite apenas números.')

    numero = int(numero_str)

    return numero


while True:
    try:
        numero1_str = input('Digite o primeiro número: ')
        numero1 = valida_numero(numero1_str)

        numero2_str = input('Digite o segundo número: ')
        numero2 = valida_numero(numero2_str)

        numero3_str = input('Digite o terceiro número: ')
        numero3 = valida_numero(numero3_str)

        if numero1 > numero2 and numero1 > numero3:
            print('O maior número é o primeiro')
        elif numero2 > numero1 and numero2 > numero3:
            print('O maior número é o segundo')
        elif numero3 > numero1 and numero3 > numero2:
            print('O maior número é o terceiro')
        else:
            print('Os números são iguais')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
        break
