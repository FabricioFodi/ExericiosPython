# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

alturas = []
idades = []
pessoas = 5

for i in range(pessoas):
    while True:
        idade = int(input('Digite sua idade: '))
        if 0 <= idade <= 108:
            idades.append(idade)
            break
        else:
            print('Idade Inválida. Digite uma idade entre 0 à 108')
    while True:
        altura = float(input('Digite sua altura: '))
        if 0 <= altura <= 3:
            alturas.append(altura)
            break
        else:
            print('Altura Inválida. Digite uma altura de até 3m.')
            
# Obter os iteradores reversos
alturas_reversa = reversed(alturas)
idades_reversa = reversed(idades)

# Converter os iteradores em listas
alturas_reversa_lista = list(alturas_reversa)
idades_reversa_lista = list(idades_reversa)

# Exibir as listas em ordem reversa
print(f"Altura das pessoas inversa: {alturas_reversa_lista}")
print(f"Idade das pessoas inversa: {idades_reversa_lista}")
