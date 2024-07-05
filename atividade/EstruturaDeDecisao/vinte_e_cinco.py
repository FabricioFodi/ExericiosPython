# Exercício 25
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def validar_pergunta(pergunta):
    resposta = pergunta.strip().lower()

    if resposta not in {'sim', 's', 'não', 'nao', 'n'}:
        raise ValueError('Resposta inválida.')

    return resposta


contador = 0
while True:
    try:
        pergunta0 = input('Telefonou para a vítima? ')
        resposta0 = validar_pergunta(pergunta0)
        if resposta0 in {'sim', 's'}:
            contador += 1
        pergunta1 = input('Esteve no local do crime? ')
        resposta1 = validar_pergunta(pergunta1)
        if resposta0 in {'sim', 's'}:
            contador += 1
        pergunta2 = input('Mora perto da vítima? ')
        resposta2 = validar_pergunta(pergunta2)
        if resposta0 in {'sim', 's'}:
            contador += 1
        pergunta3 = input('Devia para a vítima? ')
        resposta3 = validar_pergunta(pergunta3)
        if resposta0 in {'sim', 's'}:
            contador += 1
        pergunta4 = input('Já trabalhou com a vítima? ')
        resposta4 = validar_pergunta(pergunta4)
        if resposta0 in {'sim', 's'}:
            contador += 1

        if contador == 2:
            print(f'Repondeu "sim" para {contador} perguntas.\nClassificação: Suspeito')
        elif 3 <= contador <= 4:
            print(f'Repondeu "sim" para {contador} perguntas.\nClassificação: Cúmplice')
        elif contador == 5:
            print(f'Repondeu "sim" para {contador} perguntas.\nClassificação: Assasino')
        else:
            print(f'Repondeu "sim" para {contador} perguntas.\nClassificação: Inocente')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário.')
        break
