# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados
# em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados

import random


def simula_lancamento_dados(n_lancamentos):
    resultados = []
    for _ in range(n_lancamentos):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados


def conta_resultados(resultados):
    contadores = [0] * 6
    for resultado in resultados:
        contadores[resultado - 1] += 1
    return contadores


def main():
    n_lancamentos = 100
    resultados = simula_lancamento_dados(n_lancamentos)
    contadores = conta_resultados(resultados)

    print("Resultado dos lançamentos:")
    for i in range(6):
        print(f"Número {i + 1}: {contadores[i]} vezes")


if __name__ == "__main__":
    main()
