# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

# Função para validar entradas numéricas
def valida_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")


def valida_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            codigos = []
            alturas = []
            pesos = []

            while True:
                codigo = valida_int("Digite o código do cliente (0 para encerrar): ")
                if codigo == 0:
                    break
                altura = valida_float("Digite o altura do cliente (m): ")
                peso = valida_float("Digite o peso do cliente: ")

                codigos.append(codigo)
                alturas.append(altura)
                pesos.append(peso)

            if len(codigos) == 0:
                print('Nenhum dado foi inserido.')
            else:
                mais_alto = max(alturas)
                mais_baixo = min(alturas)
                mais_gordo = max(pesos)
                mais_magro = min(pesos)

                codigo_mais_alto = codigos[alturas.index(mais_alto)]
                codigo_mais_baixo = codigos[alturas.index(mais_baixo)]
                codigo_mais_gordo = codigos[pesos.index(mais_gordo)]
                codigos_mais_magro = codigos[pesos.index(mais_magro)]

                media_altura = sum(alturas) / len(alturas)
                media_peso = sum(pesos) / len(pesos)

                print(f'\nCliente mais alto: Código {codigo_mais_alto}. Altura: {mais_alto:.2f}m')
                print(f'Cliente mais baixo: Código {codigo_mais_baixo}. Altura: {mais_baixo:.2f}m')
                print(f'Cliente mais gordo: Códgio {codigo_mais_gordo}. Peso: {mais_gordo:.2f}kg')
                print(f'Cliente mais magro: Código {codigos_mais_magro}. Peso: {mais_magro:.2f}kg')
                print(f"Média de altura dos clientes: {media_altura:.2f}m")
                print(f"Média de peso dos clientes: {media_peso:.2f}kg")
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
