# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

def serie(variavel):
    soma = 0
    h = 'H = '
    for i in range(1, variavel + 1):
        h += f'1/{i} + ' if i < variavel else f'1/{i}'
        resultado = 1 / i
        soma += resultado
    print(h)
    print(f'Soma: {soma:.2f}')

    return soma


variavel = int(input('Digite um valor: '))
serie(variavel)

