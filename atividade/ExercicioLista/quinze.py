# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

vetor = []

while True:
    numero = float(input('Informe um número: '))
    if numero != -1:
        vetor.append(numero)
    else:
        break
print(f'Quantidade de valores lidos: {len(vetor)}')
print(f'Valores um ao lado do outro: {vetor}')
print(f'Valores na ordem inversa, um abaixo do outro:')
for numero in reversed(vetor):
    print(numero)
soma = sum(vetor)
print(f'A soma dos valores lidos: {soma}')
media = soma / len(vetor)
print(f'A media dos valores lidos: {media}')
valores_acima_da_media = len([i for i in vetor if i > media])
print(f'Valores acima da média: {valores_acima_da_media}')
valores_abaixo_de_sete = len([i for i in vetor if i < 7])
print(f'Valores abaixo de 7: {valores_abaixo_de_sete}')
print('Fim do programa.')