# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.


def valida_cao(n_str):
    try:
        return float(n_str)
    except ValueError:
        return None


def main():
    numeros = []
    for i in range(10):
        while True:
            n_str = input(f'Informe o {i + 1}° número:')
            n = valida_cao(n_str)
            if n is not None:  # Só adiciona o número se for válido
                numeros.append(n)
                break

    numeros.reverse()
    print(numeros)


if __name__ == '__main__':
    main()
