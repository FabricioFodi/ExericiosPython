# Exercício 13
# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

def valida_escolha(escolha):
    if escolha not in [1, 2, 3, 4, 5, 6, 7]:
        raise ValueError('Escolha entre uma dessas opções.')
    return escolha

while True:
    try:
        escolha = int(input('Digite de 1 a 7: '))
        valida_escolha(escolha)
        print(f'Você escolheu {escolha}')
        if escolha == 1:
            print('Domingo')
        elif escolha == 2:
            print('Segunda-feira')
        elif escolha == 3:
            print('Terça-feira')
        elif escolha == 4:
            print('Quarta-feira')
        elif escolha == 5:
            print('Quinta-feira')
        elif escolha == 6:
            print('Sexta-feira')
        elif escolha == 7:
            print('Sábado')
        break

    except ValueError as ve:
        print(f'Erro {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break

