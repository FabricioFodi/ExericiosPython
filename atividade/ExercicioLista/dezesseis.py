# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
# ou seja, um total de $470. Escreva um programa (usando um array de contadores)
# que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

def calcular_salario(vendas_brutas):
    salario_base = 200
    comissao = 0.09
    return salario_base + vendas_brutas * comissao


def main():
    # Lista para contar os salários nas faixas desejadas
    contadores = [0] * 9  # 9 faixas, de $200-$299 até $1000 e acima

    while True:
        try:
            vendas_brutas = float(input("Digite o valor das vendas brutas ou -1 para sair: "))
            if vendas_brutas == -1:
                break

            salario = calcular_salario(vendas_brutas)
            print(f"Salário calculado: ${salario:.2f}")

            if salario >= 1000:
                contadores[8] += 1
            else:
                posicao = int((salario - 200) // 100)
                contadores[posicao] += 1

        except ValueError:
            print("Por favor, insira um número válido.")

    # Imprime os resultados
    faixas = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599", "$600 - $699", "$700 - $799", "$800 - $899",
              "$900 - $999", "$1000 e acima"]
    for i in range(len(contadores)):
        print(f"{faixas[i]}: {contadores[i]} vendedores")


if __name__ == "__main__":
    main()
