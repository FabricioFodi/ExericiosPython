# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
# bem como a média das temperaturas.


def valida_entrada(n_str):
    if not n_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor inválido.')
    return float(n_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            termos = []

            while True:
                try:
                    n_str = input("Digite uma temperatura (ou 0 para parar): ")
                    n = valida_entrada(n_str)
                    if n == 0:
                        break
                    termos.append(n)
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')

            if termos:
                menor = min(termos)
                maior = max(termos)
                media = sum(termos) / len(termos)
                print(f'Menor temperatura: {menor}')
                print(f'Maior temperatura: {maior}')
                print(f'Média das temperaturas: {media:.2f}')
            else:
                print("Nenhuma temperatura foi inserida.")

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



