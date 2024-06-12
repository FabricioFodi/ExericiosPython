# Exercício 1
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


def valida_nota(nota_str):
    try:
        nota = float(nota_str)

        if nota < 0 or nota > 10:
            raise ValueError('A quantidade deve ser maior que zero.')
    except ValueError:
        raise ValueError('Quantidade inválida. Informe um número válido.')
    return nota


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"

while True:
    try:
        nota_str = input('Informe uma nota: ')
        nota = valida_nota(nota_str)

        print(f'sua nota é: {nota}')

        break
    except ValueError as ve:
        print(f'    {RED}>Erro: {ve}{RESET}\n')
