# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
# projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva,
# a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: a.Cada
# funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais,
# isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve
# ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
# salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor
# do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá
# apresentar:
# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono;
# A tela abaixo é um exemplo de execução do programa, apenas para
# fins ilustrativos. Os valores podem mudar a cada execução do programa.
#
# Projeção de Gastos com Abono
# ============================
#
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
#
# Salário    - Abono
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00
#
# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

def calcula_abono(salario):
    abono = max(0.2 * salario, 100)  # 20% do salário ou o mínimo de 100
    return abono

RED = "\033[91m"
RESET = "\033[0m"
BROWN = "\033[0;33m"


def main():
    salarios = []
    abonos = []
    total_abonos = 0
    valor_minimo = 100
    num_minimo = 0
    print("Projeção de Gastos com Abono")
    print("============================")

    while True:
        try:
            salario_str = input('Informe seu salário(0=fim): ')
            salario = float(salario_str)
            if salario == 0:
                break
            salarios.append(salario)
        except ValueError as ve:
            print(f'{RED}Erro: {ve}{RESET}\n')
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            raise SystemExit

    for salario in salarios:
        abono = calcula_abono(salario)
        abonos.append(abono)
        total_abonos += abono
        if abono <= valor_minimo:
            num_minimo += 1

    print('\nSalário    - Abono')
    for salario, abono in zip(salarios, abonos):
        print(f'R$ {salario:8.2f} - R$ {abono:8.2f}')

    print(f"\nForam processados {len(salarios)} colaboradores")
    print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
    print(f"Valor mínimo pago a {num_minimo} colaboradores")
    print(f"Maior valor de abono pago: R$ {max(abonos):.2f}")


if __name__ == '__main__':
    while True:
        try:
            main()
            resposta = input(f'{BROWN}Quer continuar? [S/N]{RESET}: ')
            if resposta.lower() != 's':
                print(f'{BROWN}Programa finalizado.{RESET}')
                break
        except KeyboardInterrupt:
            print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
            break
