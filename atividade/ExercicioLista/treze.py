# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

nome_todos_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media_anual = 0
media_mes = []


for i, mes in enumerate(nome_todos_meses, start=1):
    temperatura = int(input(f'Informe a temperatura média referente a {i} - {mes}: '))
    media_mes.append(temperatura)

media_anual = sum(media_mes)/len(media_mes)
print(f'Média: {media_anual}:.2f')
print('Meses com temperaturas acima da média anual:')
for i, mes in enumerate(nome_todos_meses):
    if media_mes[i] > media_anual:
        print(f'{i + 1} - {mes}: {media_mes[i]}°C')

