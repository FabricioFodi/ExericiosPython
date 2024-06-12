# Exercício 19
# Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros.
# Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades

def valida_numero(numero_str):
    if not numero_str.isdigit():
        raise ValueError('Valor inválido')

    numero = int(numero_str)

    if numero >= 1000:
        raise ValueError("Digite um número menor que 1000")

    return numero

while True:
    try:
        numero_str = input('Informe um número: ')
        numero = valida_numero(numero_str)

        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = numero % 10

        partes = [] # lista vazia para armazenar as partes da descrição do número

        if centena > 0:
            partes.append(f'{centena} centena{"s" if centena > 1 else ""}')
        if dezena > 0:
            partes.append(f'{dezena} dezena{"s" if dezena > 1 else ""}')
        if unidade > 0:
            partes.append(f'{unidade} unidade{"s" if unidade > 1 else ""}')

        if not partes:
            print("O número é zero.")
        else: # Se há mais de uma parte, formata a saída com vírgulas e "e"
            if len(partes) > 1:
                # Junta todos os elementos exceto o último com ', ' e depois adiciona ' e ' antes do último
                resultado = ', '.join(partes[:-1]) + ' e ' + partes[-1]
            else:
                # Se há apenas uma parte, não adiciona vírgulas ou 'e'
                resultado = partes[0]

            print(f"Este número tem {resultado}")
        break

    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompida pelo usuário')
        break
