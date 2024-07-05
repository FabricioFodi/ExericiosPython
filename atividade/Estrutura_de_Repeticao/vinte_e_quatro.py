# Faça um programa que calcule o mostre a média aritmética de N notas.

def valida_nota_valor(valor_str):
    if not valor_str.isdigit():
        raise ValueError("Formato de nota inválido. Deve ser um número entre 0 e 10.")

    valor = float(valor_str.replace(",", "."))
    if valor < 0 or valor > 10:
        raise ValueError("Nota inválida. Deve estar entre 0 e 10.")

    return valor


def calcula_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


def main():
    while True:
        try:
            while True:
                try:
                    numero_notas_str = input("Informe o número de notas: ")
                    numero_notas = int(numero_notas_str)
                    if numero_notas > 0:
                        break
                    else:
                        raise ValueError("Número de notas inválido. Deve ser maior que 0.")
                except ValueError as ve:
                    print(f"Erro: {ve}")

            notas = []
            for i in range(1, numero_notas + 1):
                while True:
                    try:
                        nota_str = input(f"Informe a {i}ª nota: ")
                        nota = valida_nota_valor(nota_str)
                        notas.append(nota)
                        break
                    except ValueError as ve:
                        print(f"Erro: {ve}")

            media = calcula_media(notas)
            print(f"Sua média final: {media:.2f}")
            break

        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário.")
            raise SystemExit

    while True:
        try:
            resposta = input("Quer continuar? [S/N]: ").lower()
            if resposta != "s":
                print("Programa finalizado.")
                break
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário.")
            break


if __name__ == "__main__":
    main()