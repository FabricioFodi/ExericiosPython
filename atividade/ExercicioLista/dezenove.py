# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
# organizações: "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa
# que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o
# programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem
# sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o
# vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

sistema_operacional = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']


def valida_votacoa(votos_str):
    try:
        voto = int(votos_str)
        if voto == 0 or (1 <= voto <= 6):
            return voto
        else:
            raise ValueError('Informe um valor entre 1 e 6 ou 0 para sair')
    except ValueError:
        raise ValueError('Voto inválido')


def calcula_porcentagem(votos_OS, total_votos):
    return (votos_OS / total_votos) * 100


RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    print('1- Windows Server'
          '\n2- Unix'
          '\n3- Linux'
          '\n4- Netware'
          '\n5- Mac OS'
          '\n6- Outro')
    votos = []
    while True:
        try:
            votos_str = input(f'Informe seu voto(0=fim): ')
            voto = valida_votacoa(votos_str)
            if voto == 0:
                break
            votos.append(voto)
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit

    total_votos = len(votos)
    print('\nnResultado da votação:')
    print(f'Foram computados {total_votos} votos')
    print(f'{"Sistema Operacional":>15} {"Votos":>10} {"%":>8}')

    contagem_votos = [0] * 6
    for voto in votos:
        contagem_votos[voto - 1] += 1

    melhor_os = None
    max_votos = 0

    for idx, num_votos in enumerate(contagem_votos):
        if num_votos > 0:
            percentual = calcula_porcentagem(num_votos, total_votos)
            print(f'{sistema_operacional[idx]:>15} {num_votos:>10} {percentual:>15.1f}%')
            if num_votos > max_votos:
                max_votos = num_votos
                melhor_os = idx

    if melhor_os is not None:
        melhor_percentual = calcula_porcentagem(max_votos, total_votos)
        print(f'\nO Melhor Sistema Operacional para Servidores é: {sistema_operacional[melhor_os]}')
        print(f'Com {max_votos} votos, correspondendo a {melhor_percentual:.1f}% dos votos.')


if __name__ == '__main__':
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
