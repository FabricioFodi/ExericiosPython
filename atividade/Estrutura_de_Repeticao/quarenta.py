# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cod_cidades = [11, 21, 47, 55, 81]
veiculos_de_passeio = [98593, 52530, 19895, 29635, 32152]
acidentes = [5320, 3842, 1053, 1536, 1983]

# Criando um dicionário
dados = {(veiculos, acidente): codigo for veiculos, acidente, codigo in zip(veiculos_de_passeio, acidentes, cod_cidades)}

# Imprimindo o dicionário
for (veiculos, acidente), codigo in dados.items():
    print(f"Veículos de passeio: {veiculos}, Acidentes: {acidente}, DDD: {codigo}")

maior_indice = max(acidentes)
menor_indice = min(acidentes)

media_veiculos = sum(veiculos_de_passeio) / len(veiculos_de_passeio)
media_acidente = sum(acidentes) / len(acidentes)
print(f"Maior indice de acidentes: {maior_indice}\nMenor indice de acidentes: {menor_indice}")
print(f'Média de veículos de todas as cidades: {media_veiculos}')
print(f"Media de acidentes de todas as cidades: {media_acidente}")
