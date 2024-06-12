# Exercício 22
# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

def valida_numero(numero_str):
    if not numero_str.isdigit():
        raise ValueError("Valor inválido")

    numero = int(numero_str)

    if numero <= 0:
        raise ValueError('O número precisa ser maior que zero')

    return numero

while True:
    try:
        numero_str = input('Infomre um valor: ')
        numero = valida_numero(numero_str)
        if numero % 2 == 0:
            print('Este número é par')
        else:
            print('Este número é impar')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário')
        break