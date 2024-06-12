# Exercício 10
# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def validar(letra):
    if letra not in ["M", "V", "N"]:
        raise TypeError("Digite um Caractér válido.")
    return letra

while True:
    try:
        letra = input("Digite o turno em que você estuda.\nM-Matutino\nV-Vespestino\nN-Noturno\nR: ").upper()
        letra = validar(letra)
        if letra == 'M':
            print('Bom Dia')
        elif letra == 'V':
            print('Boa Tarde')
        elif letra == 'N':
            print('Boa Noite')

        break
    except TypeError as te:
        print(f'Erro: {te}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break