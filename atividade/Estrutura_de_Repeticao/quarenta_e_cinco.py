# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito
# da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
#
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor
# digite o gabarito da prova antes dos alunos usarem o programa.


# Gabarito predefinido
gabarito = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']


# Função para verificar respostas
def verificar_respostas(respostas, gabarito):
    acertos = 0
    for resposta, correta in zip(respostas, gabarito):
        if resposta.upper() == correta:
            acertos += 1
    return acertos


# Função principal
def main():
    notas = []
    while True:
        print("\nProva com 10 questões. Insira suas respostas (A, B, C, D).")
        respostas = []

        for i in range(10):
            while True:
                resposta = input(f"Resposta da questão {i + 1}: ").upper()
                if resposta in ['A', 'B', 'C', 'D']:
                    respostas.append(resposta)
                    break
                else:
                    print("Resposta inválida. Insira A, B, C ou D.")

        acertos = verificar_respostas(respostas, gabarito)
        notas.append(acertos)
        print(f"\nVocê acertou {acertos} questões.")
        print(f"Sua nota é: {acertos}/10")

        outro_aluno = input("\nOutro aluno vai utilizar o sistema? (S/N): ").upper()
        if outro_aluno != 'S':
            break

    # Após todos os alunos terem respondido
    if notas:
        maior_acerto = max(notas)
        menor_acerto = min(notas)
        total_alunos = len(notas)
        media_notas = sum(notas) / total_alunos

        print("\nResumo da turma:")
        print(f"Maior acerto: {maior_acerto}")
        print(f"Menor acerto: {menor_acerto}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Média das notas: {media_notas:.2f}")
    else:
        print("Nenhum aluno respondeu a prova.")


if __name__ == "__main__":
    main()
