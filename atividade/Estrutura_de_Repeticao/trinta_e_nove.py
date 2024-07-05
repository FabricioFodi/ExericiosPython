# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.


def valida_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                raise ValueError ('Valor inválido')
            return valor
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro')


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


codigos = []
alturas = []


def main():
    while True:
        try:
            while True:
                codigo = int(input('Digite o código do aluno (0 para encerrar):'))
                if codigo == 0:
                    break
                altura = int(input('Digite a altura do aluno (CM):'))

                codigos.append(codigo)
                alturas.append(altura)

            if len(codigos) == 0:
                print('Nenhum dado foi inserido.')
            else:
                mais_alto = max(alturas)
                mais_baixo = min(alturas)

                codigo_mais_alto = codigos[alturas.index(mais_alto)]
                codigo_mais_baixo = codigos[alturas.index(mais_baixo)]

            print(f'\nAluno mais alto: Código {codigo_mais_alto}, Altura: {mais_alto}')
            print(f'Aluno mais baixo: {codigo_mais_baixo}, Altura: {mais_baixo}')
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
