# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"

def main():
    numeros = []
    pares = 0
    impares = 0
    for i in range(10):
        while True:
            try:
                respostas = int(input(f'Informe o {i +1}° número: '))
                numeros.append(respostas)

                if respostas % 2 == 0:
                    pares += 1
                else:
                    impares += 1
                break
            except ValueError as ve:
                print(f'{RED}Erro: Informe um valor válido.{RESET}\n')
            except KeyboardInterrupt:
                print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
                raise SystemExit
    print(f'Valores pares: {pares}\nValores impares: {impares}')

while True:
    try:
        main()
        resposta = input(f'{BROWN}Quer continuar? [S/N]{RESET}: ')
        if resposta.lower() != 's':
            print(f'{BROWN}Programa finalizado.{RESET}')
            break
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
