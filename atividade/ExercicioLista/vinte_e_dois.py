# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses
# que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
# número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera; necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma
# identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório: Quantidade
# de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

def main():
    # Inicializa os contadores
    total_mouses = 0
    defeitos = [0, 0, 0,
                0]  # [necessita da esfera, necessita de limpeza, troca do cabo ou conector, quebrado ou inutilizado]

    print("Registro de levantamento de mouses")
    print("Para encerrar o programa, digite 0 como identificação do mouse.\n")

    while True:
        try:
            identificacao = int(input("Número de identificação do mouse: "))
            if identificacao == 0:
                break

            print("Tipos de defeito:")
            print("1- necessita da esfera")
            print("2- necessita de limpeza")
            print("3- necessita troca do cabo ou conector")
            print("4- quebrado ou inutilizado")

            tipo_defeito = int(input("Tipo de defeito: "))

            if 1 <= tipo_defeito <= 4:
                defeitos[tipo_defeito - 1] += 1
                total_mouses += 1
            else:
                print("Tipo de defeito inválido. Tente novamente.\n")

        except ValueError:
            print("Entrada inválida. Tente novamente.\n")

    # Calcula os percentuais
    percentuais = [(count / total_mouses) * 100 for count in defeitos]

    # Gera o relatório
    print("\nRelatório Final")
    print(f"Quantidade de mouses: {total_mouses}")
    print("Situação                        Quantidade              Percentual")
    situacoes = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector",
                 "quebrado ou inutilizado"]
    for i in range(4):
        print(f"{i + 1}- {situacoes[i]:<30} {defeitos[i]:<10} {percentuais[i]:.2f}%")


if __name__ == "__main__":
    main()

