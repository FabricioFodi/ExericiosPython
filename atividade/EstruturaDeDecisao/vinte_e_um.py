# Exercício 21
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
#  e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais,
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def valida_soma(valor_str):
    if not valor_str.isdigit():
        raise ValueError('Valor inválido')

    valor = int(valor_str)

    if valor < 10:
        raise ValueError('Valor abaixo. Por favor informe um valor de no mínimo R$10')

    if valor > 3000:
        raise ValueError('Valor Excedido. Por favor informe um valor menor')
    return valor


while True:
    try:
        valor_str = input('Digite o valor do saque: ')
        valor = valida_soma(valor_str)

        nota100 = valor // 100
        valor %= 100 # atualiza o valor utilizando % (módulo)
        nota50 = valor // 50
        valor %= 50 # atualiza o valor utilizando % (módulo)
        nota20 = valor // 20
        valor %= 20 # atualiza o valor utilizando % (módulo)
        nota10 = valor // 10
        valor %= 10 # atualiza o valor utilizando % (módulo)
        nota5 = valor // 5
        valor %= 5 # atualiza o valor utilizando % (módulo)
        nota2 = valor // 2
        valor %= 2 # atualiza o valor utilizando % (módulo)
        nota1 = valor  # O restante será a quantidade de notas de 1

        partes = []

        if nota100 > 0:
            partes.append(f'{nota100} nota{"s" if nota100 > 1 else ""} de 100')
        if nota50 > 0:
            partes.append(f'{nota50} nota{"s" if nota50 > 1 else ""} de 50')
        if nota20 > 0:
            partes.append(f'{nota20} nota{"s" if nota20 > 1 else ""} de 20')
        if nota10 > 0:
            partes.append(f'{nota10} nota{"s" if nota10 > 1 else ""} de 10')
        if nota5 > 0:
            partes.append(f'{nota5} nota{"s" if nota5 > 1 else ""} de 5')
        if nota2 > 0:
            partes.append(f'{nota2} nota{"s" if nota2 > 1 else ""} de 2')
        if nota1 > 0:
            partes.append(f'{nota1} nota{"s" if nota1 > 1 else ""} de 1')

        if not partes:
            print("O número é zero.")
        else:  # Se há mais de uma parte, formata a saída com vírgulas e "e"
            if len(partes) > 1:
                # Junta todos os elementos exceto o último com ', ' e depois adiciona ' e ' antes do último
                resultado = ', '.join(partes[:-1]) + ' e ' + partes[-1]
            else:
                # Se há apenas uma parte, não adiciona vírgulas ou 'e'
                resultado = partes[0]

            print(f"O saque terá: {resultado}")
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('\nOperação interrompida pelo usuário.')
        break
