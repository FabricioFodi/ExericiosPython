# Exercício 4
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média bimestral do aluno é {media:.1f}")
# f"{media:.1f}": Usa uma f-string para formatar o valor de media diretamente na string, com uma casa decimal.
