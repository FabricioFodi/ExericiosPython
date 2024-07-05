# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.
# Para finalizar o conjunto de votos tem-se o valor zero.

import sys


def valida_voto(voto_str):
    if voto_str == '':
        sys.exit()
    if voto_str not in ['0', '1', '2', '3', '4', '5', '6']:
        raise ValueError('Voto inválido')
    return int(voto_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"

intervalos = {
    '1': 'José',
    '2': 'João',
    '3': 'Maria',
    '4': 'Ana',
    '5': 'Voto Nulo',
    '6': 'Voto em Branco'
}
votos = {key: 0 for key in intervalos.keys()}

print(f"{'Candidato':<20} {'Código':<6}")
for codigo, candidato in intervalos.items():
    print(f"{candidato:<20} {codigo:<6}")


def main():
    while True:
        try:
            voto_str = input('Informe seu voto (ou 0 para encerrar): ')
            voto = valida_voto(voto_str)
            if voto == 0:
                break
            votos[str(voto)] += 1
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            sys.exit()

    print("\nResultado da votação:")
    for codigo, quantidade in votos.items():
        print(f"{intervalos[codigo]:<20} {quantidade}")


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
