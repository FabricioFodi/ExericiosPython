# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu
# gerar o seguinte arquivo, chamado "usuarios.txt": alexandre       456123789 anderson        1245698456 antonio
# 123456456 carlos          91257581 cesar           987458 rosemary        789456125 Neste arquivo,
# o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório,
# chamado "relatório.txt", no seguinte formato: ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------ Nr.  Usuário        Espaço utilizado     %
# do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB Espaço médio ocupado: 430,26 MB O arquivo de entrada deve ser lido uma única vez,
# e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão
# da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada,
# que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma
# função, que será chamada pelo programa principal.

import os


# Função para criar o arquivo 'usuarios.txt'
def criar_arquivo_usuarios(filename):
    dados = """\
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
"""
    with open(filename, 'w') as file:
        file.write(dados)


def ler_arquivo(filename):
    usuarios = []
    with open(filename, 'r') as file:
        for line in file:
            nome = line[:15].strip()
            espaco = int(line[15:].strip())
            usuarios.append((nome, espaco))
    return usuarios


def converter_para_mb(tamanho_bytes):
    return tamanho_bytes / (1024 * 1024)


def calcular_percentual(espaco_utilizado, espaco_total):
    return (espaco_utilizado / espaco_total) * 100


def gerar_relatorio(usuarios, filepath):
    total_espaco = sum(user[1] for user in usuarios)
    relatorio = []
    relatorio.append("ACME Inc.               Uso do espaço em disco pelos usuários")
    relatorio.append("------------------------------------------------------------------------")
    relatorio.append("Nr.  Usuário        Espaço utilizado     % do uso\n")

    for i, (nome, espaco) in enumerate(usuarios, start=1):
        espaco_mb = converter_para_mb(espaco)
        percentual = calcular_percentual(espaco, total_espaco)
        relatorio.append(f"{i:<4} {nome:<15} {espaco_mb:>8.2f} MB {percentual:>16.2f}%")

    espaco_total_mb = converter_para_mb(total_espaco)
    espaco_medio_mb = espaco_total_mb / len(usuarios)

    relatorio.append(f"\nEspaço total ocupado: {espaco_total_mb:.2f} MB")
    relatorio.append(f"Espaço médio ocupado: {espaco_medio_mb:.2f} MB")

    with open(filepath, 'w') as file:
        file.write('\n'.join(relatorio))


def main():
    # Caminho absoluto para o arquivo 'usuarios.txt'
    caminho_arquivo_usuarios = r'C:\Users\fabricio\Pasta_Projetos\ExericiosPython\atividade\ExercicioLista\usuarios.txt'

    # Cria o arquivo 'usuarios.txt'
    criar_arquivo_usuarios(caminho_arquivo_usuarios)

    # Lê os dados do arquivo 'usuarios.txt'
    usuarios = ler_arquivo(caminho_arquivo_usuarios)

    # Caminho onde o relatório será salvo
    caminho_relatorio = os.path.join(r'C:\Users\fabricio\Desktop', 'relatório.txt')
    gerar_relatorio(usuarios, caminho_relatorio)


if __name__ == "__main__":
    main()

