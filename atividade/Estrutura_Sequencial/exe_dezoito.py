# Exercício 18
# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe
# o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arquivo =  float(input("Informe o tamanho do arquivo em MB: "))
vel_internet = int(input("informe a velocidade da sua internet em MBps: "))

div = tam_arquivo / vel_internet

minutos = int(div // 60)
segundos = int(div % 60)

# Formata os minutos e segundos para duas casas decimais
minutos_formatados = f"{minutos:02}"
segundos_formatados = f"{segundos:02}"

# Exibe o resultado
print(f"Seu download demorará cerca de {minutos_formatados}:{segundos_formatados} segundos")

