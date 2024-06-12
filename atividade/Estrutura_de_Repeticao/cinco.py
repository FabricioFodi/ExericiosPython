# Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def validaEntrada(populacao_string):
    if not populacao_string.isdigit():
        raise ValueError('Erro. Por favor insira um número válido')
    return int(populacao_string)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            populacao_a_string = input('\nInforme a população total do País A: ')
            populacao_a = validaEntrada(populacao_a_string)
            populacao_b_string = input('Informe a população total do País B: ')
            populacao_b = validaEntrada(populacao_b_string)

            if populacao_a > populacao_b:
                print(
                    f'{RED}Impossível realizar cálculo. \nA taxa de crescimento do País A é maior que do País B.{RESET}')
            else:
                for anos in range(populacao_b):
                    populacao_a *= 1.03
                    populacao_b *= 1.015
                    if populacao_a >= populacao_b:
                        break
                print(f'demorará {anos} anos para que o País A atinga o número de habitantes do País B')
                print(
                    f"A população do país A é de {'{:.2f} milhões de habitntes'.format(populacao_a / 1_000_000) if populacao_a >= 1_000_000 else '{:.0f} mil de habitantes'.format(populacao_a / 1_000)}")
                print(
                    f"A população do país B é de {'{:.2f} milhões de habitantes'.format(populacao_b / 1_000_000) if populacao_b >= 1_000_000 else '{:.0f} mil de habitantes '.format(populacao_b / 1_000)}")
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}\n')
            raise SystemExit


while True:
    main()
    resposta = input(f'{BROWN}  Deseja repetir a ação? (s/n){RESET}: ')
    if resposta.lower() != 's':
        break
