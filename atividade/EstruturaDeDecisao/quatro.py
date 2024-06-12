# Exercício 4
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# A partir deste exercício tentarei usar tratamento de erros em todos os exercícios

def valida_letra(letra):
    if len(letra) != 1 or not letra.isalpha():
        return False
    return True

while True:
    try:
        letra = input('Digite uma letra: ').lower()
        if not valida_letra(letra):
            raise ValueError('Digíte apenas letras')
    except ValueError as ve:
        print(ve)
    else:
        break

if letra in 'aeiou':
    print('É vogal')
else:
    print('É consoante')