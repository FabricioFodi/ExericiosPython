# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
# que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
# a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e
# depois calcular a média). Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():

    saltos_nomes = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    nomes = []
    while True:
        try:
            saltos = []
            while True:

                nome = input('Informe o nome do atleta: ')
                if not nome.replace(' ', '', 1).isalpha():
                    print(f'{RED}Nome inválido{RESET}')
                else:
                    nomes.append(nome)
                    break

            for i in range(5):
                while True:
                    salto = input(f'{saltos_nomes[i]} Salto: ')
                    if salto.replace('.', '', 1).isdigit():
                        saltos.append(float(salto))
                        break
                    else:
                        print(f'{RED}Insira um número válido{RESET}')

            maior_salto = max(saltos)
            menor_salto = min(saltos)

            remover_extremos = saltos.copy()
            remover_extremos.remove(maior_salto)
            remover_extremos.remove(menor_salto)
            media_notas = sum(remover_extremos) / len(remover_extremos)

            print(f'{BROWN}\nAtleta: {nomes[-1]}{RESET}\n')
            for i in range(5):
                print(f'{saltos_nomes[i]} salto: {saltos[i]}m')

            # Exibe todos os saltos juntos
            print(f'\nMelhor salto: {maior_salto}m')
            print(f'Pior salto: {menor_salto}m')
            print(f'Média dos demais saltos: {media_notas:.2f}m')
            print(f'\nResultado Final:')
            print(f'{nomes[-1]}: {media_notas:.2f}m')

            continuar = input('Outro atleta vai utilizar o sistema? (S/N): ')
            if continuar.lower() != 's':
                print('Programa finalizado.')
                break
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário{RESET}')
            break


if __name__ == '__main__':
    main()
