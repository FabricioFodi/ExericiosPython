# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def valida_Voto(voto_str):
    if voto_str not in ['1', '2', '3']:
        raise ValueError('Voto invalido. Esoclha entre 1, 2 ou 3')
    return int(voto_str)


def valida_eleitores(eleitores_str):
    if not eleitores_str.isdigit():
        raise ValueError('Eleitores invalido')
    return int(eleitores_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            while True:
                try:
                    eleitores_str = input('Qual número total de eleitores? ')
                    eleitores = valida_eleitores(eleitores_str)
                    break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')


            opcao_voto_um = 0
            opcao_voto_dois = 0
            opcao_voto_tres = 0
            while True:
                try:

                    for i in range(eleitores):
                        voto_str = input('Voto da {}: '.format(i + 1))
                        voto = valida_Voto(voto_str)

                        if voto == 1:
                            opcao_voto_um += 1
                        elif voto == 2:
                            opcao_voto_dois += 1
                        elif voto == 3:
                            opcao_voto_tres += 1
                    break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')

            print(f'\nResultados:')
            print(f'Opção 1: {opcao_voto_um} votos')
            print(f'Opção 2: {opcao_voto_dois} votos')
            print(f'Opção 3: {opcao_voto_tres} votos')
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
