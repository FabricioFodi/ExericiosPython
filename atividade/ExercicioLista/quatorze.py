# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


def validar_pergunta(pergunta):
    resposta = pergunta.strip().lower()
    if resposta not in {'sim', 's', 'não', 'nao', 'n'}:
        raise ValueError('Resposta inválida.')
    return resposta


def main():
    perguntas = [
        'Telefonou para a vítima?',
        'Esteve no local do crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'
    ]
    contador = 0

    try:
        for pergunta in perguntas:
            resposta = validar_pergunta(input(pergunta + ' '))
            if resposta in {'sim', 's'}:
                contador += 1

        if contador == 2:
            classificacao = 'Suspeito'
        elif 3 <= contador <= 4:
            classificacao = 'Cúmplice'
        elif contador == 5:
            classificacao = 'Assassino'
        else:
            classificacao = 'Inocente'

        print(f'Respondeu "sim" para {contador} perguntas.\nClassificação: {classificacao}')
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário.')


if __name__ == '__main__':
    main()
