# Exercício 20
# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:
#   A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   A mensagem "Aprovado com Distinção", se a média for igual a 10.

def valida_nota(nota_str):
    if not nota_str.isdigit():
        raise ValueError("Digite um valor válido.")

    nota = float(nota_str)

    if nota < 0 or nota > 10:
        raise ValueError("Nota deve ser entre 0 e 10.")

    return nota


while True:
    try:
        nota1_str = input("Informe a primeira nota:  ")
        nota1 = valida_nota(nota1_str)
        nota2_str = input("Informe a segunda nota: ")
        nota2 = valida_nota(nota2_str)
        nota3_str = input("Informe a terceira nota: ")
        nota3 = valida_nota(nota3_str)

        media = (nota1 + nota2 + nota3) / 3
        if media < 7.0:
            print(f'Reprovado!\nMédia: {media:.1f}')
        elif media >= 7.0:
            print(f'Aprovado!\nMédia: {media:.1f}')
        elif media == 10:
            print(f'Parabéns, Aprovado com distinçao\nMédia: {media:.1f}')
        break
    except ValueError as ve:
        print(f'Erro: {ve}')
    except KeyboardInterrupt:
        print('Operação interrompdiiad pelo usário.')
        break
