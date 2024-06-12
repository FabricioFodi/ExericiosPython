# Exercício 9
# Faça um Programa que leia três números e mostre-os em ordem decrescente.

def validar_numero(numero_str):
    if not numero_str.replace('.', '', 1).isdigit():
        raise TypeError('Valor invalido. Digite apenas números')

    numero = float(numero_str)

    return numero

while True:
    try:
        numero1_str =input('Escreva um número: ')
        numero1 = validar_numero(numero1_str)
        numero2_str = input('Escreva um número: ')
        numero2 = validar_numero(numero2_str)
        numero3_str = input('Escreva um número: ')
        numero3 = validar_numero(numero3_str)

        # Pedi ao chatGPT e ele me deu uma sugestão de usar o .sorted()
        # é uma maneira bem mais facil de fazer este código
        # Por padrão, .sorted() ordena os itens em ordem crescente, porém
        # se você usar "reverse = True", ele ordena em ordem decrescente.
        numeros = [numero1, numero2, numero3]

        ordem_crescente = sorted(numeros)
        print(f'Números em ordem crescente: {ordem_crescente}')

        ordem_decrescente = sorted(numeros, reverse=True) # reverse=True -> decrescente
        print(f'Números em ordem decrescente{ordem_decrescente}')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break