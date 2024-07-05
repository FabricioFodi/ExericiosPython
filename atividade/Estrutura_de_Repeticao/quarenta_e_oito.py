# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

def valida_numero(n_str):
    try:
        n = int(n_str)
        return n
    except ValueError:
        raise ValueError('Número inválido')


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    numeros = []
    while True:
        try:
            n_str = input('Informe uma sequencia de números: ')
            n = valida_numero(n_str)
            numeros.append(n)
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit

    lista_numeros = list(n_str)

    # Inverte a lista de caracteres
    lista_numeros.reverse()

    # Junta os caracteres de volta em uma string
    numero_invertido = "".join(lista_numeros)

    # Mostra o número invertido
    print(f"O número invertido é: {numero_invertido}")


if __name__ == '__main__':
    main()
