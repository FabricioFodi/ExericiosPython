# Faça um programa que leia 5 números e informe a soma e a média dos números.



def validaNumero(numero_string):
    if not numero_string.replace('.', '', 1).isdigit():
        raise ValueError("Numero invalido")
    return float(numero_string)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"

numeros = []
# Exemplo de uso
def main():
    while True:
        try:
            # Algum código que pode causar o erro
            for i in range(5):
                numero_str = input(f'Digite o {i + 1}° número: ')
                numeros.append(validaNumero(numero_str))
            soma = sum(numeros)
            media = soma / len(numeros)
                # Imprime o maior número
            print(f'A soma é: {soma}\nA média é: {media}')
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit


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
