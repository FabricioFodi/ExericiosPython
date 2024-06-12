# Exercício 17
# Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.

def valida_ano(ano_str):
    if not ano_str.isdigit():
        raise ValueError("Valor inválido.")

    ano =int(ano_str)

    if not(1720 <= int(ano_str) <= 2100):
        raise ValueError("Ano invalido.")

    return ano

while True:
    try:
        ano_str = input('Digite o ano: ')
        ano = valida_ano(ano_str)
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print('é bissexto.')
        else:
            print('não é bissexto.')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break