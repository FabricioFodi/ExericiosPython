# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


def contaDivisoes(n):
    divisoes = 0
    if n < 2:
        return False, divisoes
    for i in range(2, n):
        divisoes += 1
        if n % i == 0:
            return False, divisoes
    return True, divisoes


def main():
    while True:
        n_str = input('Digite um número: ')
        try:
            n = int(n_str)
        except ValueError:
            print('Valor inválido, por favor digite um número inteiro.')
            continue

        primos = []

        for i in range(2, n + 1):
            ePrimo, divisoes = contaDivisoes(i)
            if ePrimo:
                primos.append(i)

        print(f'Números primos entre 1 e {n}: {primos}')
        break


if __name__ == "__main__":
    main()