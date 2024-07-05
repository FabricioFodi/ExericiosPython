# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete
# jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média,
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois
# calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

def valida_nota(nota_str):
    if not nota_str.replace('.', '', 1).isdigit():
        raise ValueError('Nota inválida.')
    if nota_str <= 0 or nota_str > 10:
        raise ValueError('Nota não permitida')
    return float(nota_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33"


def main():
    juris = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto", "Sexto", "Sétimo"]
    nomes = []
    while True:
        try:
            notas = []
            while True:
                nome = input('Informe o nome do Atleta: ')
                if not nome.replace(' ', '', 1).isalpha():
                    print(f'{RED}Nome inválido{RESET}')
                else:
                    nomes.append(nome)
                    break

            for i in range(7):
                while True:
                    nota_str = input(f'{juris[i]} juri: ')
                    nota = valida_nota(nota_str)
                    notas.append(nota)
                    break

            maior_nota = max(notas)
            menor_nota = min(notas)

            remover_notas = notas.copy()
            remover_notas.remove(maior_nota)
            remover_notas.remove(menor_nota)
            media_notas = sum(remover_notas) / len(remover_notas)

            print(f'\n{BROWN}Resultado Final:{RESET}'
                  f'\nAtleta: {nomes[-1]}'
                  f'\nMelhor nota: {maior_nota}'
                  f'\nPior Nota: {menor_nota}'
                  f'\nMedia das demais notas: {media_notas}')

            continuar = input('Informar notas de outro atleta? [S/N]: ')
            if continuar.lower() != 's':
                print('Programa Finalizado')
                break
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário{RESET}')
            break


if __name__ == '__main__':
    main()
