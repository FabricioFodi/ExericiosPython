# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
# para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

def valida_produto(produto_str):
    if not produto_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor inválido.')
    return int(produto_str)


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    while True:
        try:
            lista = []
            while True:
                try:
                    print('Lojas Tabajara.')
                    produto_str = input('Digite quantos itens tem: ')
                    produto = valida_produto(produto_str)
                    break
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')

            for i in range(1, produto + 1):
                preco = float(input(f'Informe o preço do {i}º produto: '))
                lista.append(preco)
            soma = sum(lista)
            print(f'Soma dos itens: {soma}')
            while True:
                try:
                    pagamento_str = input('Pagamento em dinheiro: :')
                    pagamento = valida_produto(pagamento_str)
                    if pagamento > soma:
                        troco = pagamento - soma
                        print(f'Troco: {troco}')
                    else:
                        print(f'{RED}Está faltando dinheiro. Por favor pague o valor todo{RESET}')
                except ValueError as ve:
                    print(f'{RED}Erro: {ve}{RESET}\n')
            break
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit


while True:
    try:
        main()
        resposta = input(f'{BROWN}Quer continuar? [S/N]{RESET}: ')
        if resposta.lower() != 's':
            print(f'{BROWN}Programa finalizado.{RESET}')
            break
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
