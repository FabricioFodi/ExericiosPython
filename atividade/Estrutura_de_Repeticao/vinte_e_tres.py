# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

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

        total_divisoes = 0
        primos = []

        for i in range(2, n + 1):
            ePrimo, divisoes = contaDivisoes(i)
            total_divisoes += divisoes
            if ePrimo:
                primos.append(i)

        print(f'Números primos entre 1 e {n}: {primos}')
        print(f'Quantidade total de divisões: {total_divisoes}')
        break


if __name__ == "__main__":
    main()
