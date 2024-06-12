# Exercício 23
#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

def valida_numero(numero_str):
    numero = float(numero_str)

    if not numero_str.replace('.', '', 1).isdigit():
        raise ValueError("Valor invalido")

    return numero

while True:
    try:
        numero_str = input('Informe um número: ')
        numero = valida_numero(numero_str)
        if numero == round(numero):
            print("O número é inteiro.")
        else:
            print("O número é decimal")
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário')
        break