# Desenvolva um programa que faça a tabuada de um número qualquer inteiro
# que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
#
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35


def valida_entrada(entrada_str):
    if not entrada_str.isdigit():
        raise ValueError ('Insira um valor inteiro')
    return int(entrada_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:

            entrada1_str = input('Montar a tabuada de: ')
            montar = valida_entrada(entrada1_str)

            entrada2_str = input('Começar por: ')
            comeco = valida_entrada(entrada2_str)

            entrada3_str = input('Terminar em: ')
            termino = valida_entrada(entrada3_str)

            # Garantir que comeco seja menor ou igual a termino
            if comeco > termino:
                comeco, termino = termino, comeco

            # Garantir que termino não ultrapasse 10
            if termino > 10:
                print('Erro: O valor de "terminar em" não pode ser maior que 10.')
            else:
                print(f'Vou montar a tabuada de {montar} começando em {comeco} e terminando em {termino}')

                for i in range(comeco, termino + 1):
                    resultado = montar * i
                    print(f'{montar} x {i} = {resultado}')
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



