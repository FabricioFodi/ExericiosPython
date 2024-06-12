# Exercício 14
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

regulamento = 50
valor_multa = 4.00
excesso = 0
multa = 0

pesoPeixe = float(input("Informe o peso do peixe: "))
if pesoPeixe > regulamento:
    excesso = pesoPeixe - regulamento
    multa = valor_multa * excesso

print(f"Peso total dos peixes: {pesoPeixe} kg")
if excesso > 0:
    print(f"Excesso de peso: {excesso} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Não houve excesso de peso. Não há multa a pagar.")