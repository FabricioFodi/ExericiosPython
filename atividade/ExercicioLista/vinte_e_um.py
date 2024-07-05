# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
# VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível. Calcule e mostre: O modelo do carro mais econômico; Quantos litros de
# combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto
# custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das
# informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
# programa. Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    # Definindo constantes
    PRECO_GASOLINA = 2.25
    DISTANCIA = 1000

    # Listas para armazenar os dados
    modelos_carros = []
    consumo_carros = []
    while True:
        try:
            # Carregando os dados
            for i in range(5):
                print(f'Veículo {i + 1}')
                modelo = input('Nome: ')
                consumo = float(input('Km por litro: '))
                modelos_carros.append(modelo)
                consumo_carros.append(consumo)

            # Calculando o modelo mais econômico
            indice_mais_economico = consumo_carros.index(max(consumo_carros))
            modelo_mais_economico = modelos_carros[indice_mais_economico]

            # Gerando o relatório final
            print('\nRelatório Final')
            for i in range(5):
                litros = DISTANCIA / consumo_carros[i]
                custo = litros * PRECO_GASOLINA
                print(
                    f'{i + 1} - {modelos_carros[i]:<15} - {consumo_carros[i]:>6.1f} - {litros:>8.1f} litros - R$ {custo:>7.2f}')

            print(f'\nO menor consumo é do {modelo_mais_economico}.')
            break
        except ValueError:
            print(f'{RED}Erro:{RESET}\n')
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
