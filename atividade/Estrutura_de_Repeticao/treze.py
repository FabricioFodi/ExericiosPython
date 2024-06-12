# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

def validaNum(num_str):
    if not num_str.isdigit():
        raise ValueError('Informe um número válido.')
    return int(num_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"

while True:
    try:
        num1_str = input('Informe um número: ')
        base = validaNum(num1_str)
        num2_str = input('Informe outro número: ')
        expoente = validaNum(num2_str)

        if expoente > base:
            expoente, base = base, expoente

        potencia = base**expoente
        print(f'O resultado de {base} elevado a {expoente} é: {potencia}')
        break
        # base = 6 expoente = 3 6^3 == 6*6*6
    except ValueError as ve:
        print(f'{RED}Erro: {ve}{RESET}\n')
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break