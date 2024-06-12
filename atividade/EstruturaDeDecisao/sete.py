# Exercício 7
# Faça um Programa que leia três números e mostre o maior e o menor deles.

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

        # achei essa função max e min que encontra o maior e menor valor de um conjunto de dados
        # Então não há necessidade de fazer igual ao exercício anterior
        if numero1 == numero2 == numero3:
            print('Todos os números são iguais.')
        else:
            maior = max(numero1, numero2, numero3)
            menor = min(numero1, numero2, numero3)

            print(f'O maior número é: {maior}')
            print(f'O menor número é: {menor}')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
        break