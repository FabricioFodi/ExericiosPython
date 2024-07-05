# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

def serie_harmonica(vari):
    """
    Mostra os n termos da série harmônica e retorna a soma total.

    Args:
        vari (int): Número de termos da série.

    Returns:
        float: Soma total da série harmônica.
    """

    # Variáveis para acompanhar o termo atual e a soma parcial
    termo_atual = 1  # Começa em 1, pois 1/1 é o primeiro termo
    soma = 0

    # Loop para calcular e mostrar os termos da série
    for i in range(vari):
        # Calcular numerador e denominador do termo atual
        n = termo_atual  # Numerador é o termo atual
        m = 2 * termo_atual - 1  # Denominador: 2 * termo_atual - 1
        # Calcular o valor do termo
        termo = n / m
        # Exibir o termo formatado
        print(f"{n}/{m}")  # Ex: 1/1, 2/3, 3/5, etc.
        # Atualizar a soma parcial da série
        soma += termo
        # Incrementar o termo atual para o próximo termo
        termo_atual += 1
    # Exibir a soma total da série harmônica
    print(f"\nSoma da série: {soma:.2f}")
    # Retornar a soma total para uso posterior (opcional)
    return soma


# Solicitar o número de termos ao usuário
vari = int(input("Digite o número de termos da série: "))
# Calcular e mostrar a soma da série
serie_harmonica(vari)
