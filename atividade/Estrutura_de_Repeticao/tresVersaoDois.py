def valida_nome(nome):
    if not nome.isalpha():
        raise ValueError('Valor Inválido. Insira apenas Letras.')

    if len(nome) < 3:
        raise ValueError('Informe um nome que tenha pelo menos 3 letras.')

    return nome


def valida_idade(idade_str):
    if not idade_str.isdigit():
        raise ValueError('Valor Inválido. Insira apenas números.')

    idade = int(idade_str)

    if idade < 0 or idade >= 120:
        raise ValueError('Valor inválido. Informe um novo valor')

    return idade


def valida_salario(salario_str):
    if not salario_str.replace('.', '', 1).isdigit():
        raise ValueError('Valor inválido. Insira apenas números.')

    salario = float(salario_str)

    if salario < 0 or salario >= 36000:
        raise ValueError('Valor inválido. Informe um novo valor.')

    return salario


def valida_sexo(sexo):
    sexo = sexo.lower()
    if sexo not in ['m', 'f']:
        raise ValueError('Valor inválido. Por favor, escolha entre "F" ou "M"')

    if sexo == 'm':
        return "Masculino"
    elif sexo == 'f':
        return "Feminino"


def valida_estadocivil(estadocivil):
    estadoCivil = estadocivil.lower()
    if estadoCivil not in ['s', 'c', 'v', 'd']:
        raise ValueError('Valor Inválido. Escolha entre "S" "C" "V" ou "D" ')

    if estadoCivil == 's':
        return "Solteiro"
    elif estadoCivil == 'c':
        return "Casado"
    elif estadoCivil == 'v':
        return "Viúvo"
    elif estadoCivil == 'd':
        return "Divorciado"


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"

# Usnado um "While True" dentro do while. Com essa abordagem, cada pergunta é tratada separadamente
# e, em caso de erro, o usuário não precisa responder novamente às perguntas anteriores.

while True:
    try:
        while True:
            try:
                nome_str = input('Qual o seu nome? ')
                nome = valida_nome(nome_str)
                break
            except ValueError as ve:
                print(f'{RED}Erro: {ve}{RESET}')

        while True:
            try:
                idade_str = input('Qual a sua idade? ')
                idade = valida_idade(idade_str)
                break
            except ValueError as ve:
                print(f'{RED}Erro: {ve}{RESET}')

        while True:
            try:
                salario_str = input('Qual o seu salário? ')
                salario = valida_salario(salario_str)
                break
            except ValueError as ve:
                print(f'{RED}Erro: {ve}{RESET}')

        while True:
            try:
                sexo_str = input('Qual o seu sexo? ')
                sexo = valida_sexo(sexo_str)
                break
            except ValueError as ve:
                print(f'{RED}Erro: {ve}{RESET}')

        while True:
            try:
                estadocivil_str = input('Qual o seu estado civil? ')
                estadocivil = valida_estadocivil(estadocivil_str)
                break
            except ValueError as ve:
                print(f'{RED}Erro: {ve}{RESET}')

        print(f'\nNome: {nome_str}'
              f'\nIdade: {idade} ano{"s" if idade > 1 else ""}'
              f'\nSalário R$: {salario}'
              f'\nSexo: {sexo}'
              f'\nEstado Civil: {estadocivil}')

        break

    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
