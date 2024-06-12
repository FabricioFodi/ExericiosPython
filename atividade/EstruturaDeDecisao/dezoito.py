# Exercício 18
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime

def valida_data(data_str):
    formatos = ['%d/%m/%Y', '%d-%m-%Y', '%d %m %Y',
                '%d.%m.%Y', '%d%m%Y', '%d%m%y',
                '%Y/%m/%d', '%Y-%m-%d', '%Y%m%d']

    for formato in formatos:
        try:
            data = datetime.strptime(data_str, formato)
            return data
        except ValueError:
            continue

    raise ValueError('Formato de data invalido.')

while True:
    try:
        data_str = input('informe a data: ')
        data = valida_data(data_str)
        data_formatada = data.strftime('%d/%m/%Y')
        print(f'Data formatada: {data_formatada}')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário.')