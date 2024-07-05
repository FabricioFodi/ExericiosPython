# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
# jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
# telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a
# linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
# correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a
# pedir outro número. Após o final da votação, o programa deverá exibir: O total de votos computados; Os númeos e
# respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores; O
# número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
# votos dados a ele. Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado
# aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo
# do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um
# jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de
# exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem
# mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da
# votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela. Enquete: Quem foi o melhor
# jogador?
#
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0
#
# Resultado da votação:
#
# Foram computados 8 votos.
#
# Jogador Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

def valida_voto(voto_str):
    try:
        voto = int(voto_str)
        if voto == 0 or (1 <= voto <= 23):
            return voto
        else:
            raise ValueError('Informe um valor entre 1 e 23 ou 0 para sair')
    except ValueError:
        raise ValueError('Voto inválido')


def calcula_percentual(votos_jogador, total_votos):
    return (votos_jogador/total_votos) * 100


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    print('Enquete: Quem foi o melhor Jogador?')
    votos = []
    while True:
        try:
            voto_str = int(input('Número do jogador (0=fim): '))
            voto = valida_voto(voto_str)
            if voto == 0:
                break
            votos.append(voto)
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit

    total_votes = len(votos)
    print(f'Resultado da votação:')
    print(f'Foram computados {len(votos)} votos')
    print('Jogador\tVotos\t%')

    contagem_votos = [0] * 23
    for voto in votos:
        contagem_votos[voto - 1] += 1

    melhor_jogador = None
    max_votos = 0

    for jogador in range(1, 24):
        num_votos = contagem_votos[jogador - 1]
        if num_votos > 0:
            percentual = calcula_percentual(num_votos, total_votes)
            print(f'{jogador}\t\t{num_votos}\t\t{percentual:.1f}%')
            if num_votos > max_votos:
                max_votos = num_votos
                melhor_jogador = jogador

    if melhor_jogador is not None:
        melhor_percentual = calcula_percentual(melhor_jogador, total_votes)
        print(f'\nO melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, correspondendo a {melhor_percentual:.1f}% do total de votos.')


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
