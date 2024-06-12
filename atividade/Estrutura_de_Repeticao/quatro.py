# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento
# de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_pais_A = 80000
populacao_pais_B = 300000


#calcular em quantos anos a população do país A alcanÇara a população do país B


for anos in range(populacao_pais_B):
    populacao_pais_A *= 1.03
    populacao_pais_B *= 1.015
    if populacao_pais_A >= populacao_pais_B:
        break

print(f'demorará {anos} anos para que o País A atinga o número de habitantes do País B')
print(f"A população do país A é de {'{:.2f} milhões de habitntes'.format(populacao_pais_A / 1_000_000) if populacao_pais_A >= 1_000_000 else '{:.0f} mil de habitantes'.format(populacao_pais_A / 1_000)}")
print(f"A população do país B é de {'{:.2f} milhões de habitantes'.format(populacao_pais_B / 1_000_000) if populacao_pais_B >= 1_000_000 else '{:.0f} mil de habitantes '.format(populacao_pais_B / 1_000)}")

