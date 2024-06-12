# Exercício 7
# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o lado do quadrado: '))

area = lado ** 2

print(f"O valor da área do quadrado é: {area:.2f}m")

dobroArea = area * 2

print(f"O dobro da área é: {dobroArea:.2f}m")