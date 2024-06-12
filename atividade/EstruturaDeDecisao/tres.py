# Exercício 4
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

# versão 1

entrada = input('Digite F ou M: ')
if entrada == 'F' or entrada == 'f':
    print('Feminino')
elif entrada == 'M' or entrada == 'm':
    print('Masculino')
else:
    print('Entrada inválida')

# --------------------------------------- #

# versão 2

entrada1 = input('Digite F ou M: ').upper()

if entrada1 == 'F':
    print('Feminino')
elif entrada1 == 'M':
    print('Masculino')
else:
    print('Entrada inválida')