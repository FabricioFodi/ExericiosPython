# Exercício 3
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


def valida_nome(nome):
    if not nome.isalpha():
        raise ValueError('Valor Inválido. Insira apenas Letras.')

    if len(nome) < 3:
        raise ValueError('Informe um nome que tenhs pelo menos 3 letras.')

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
    if sexo not in ['M', 'F', 'm' , 'f']:
        raise ValueError('Valor inválido. Por favor, escolha entre "F" ou "M"')

    if sexo == 'M' or sexo == 'm':
        return "Masculino"
    elif sexo == 'F' or sexo == 'f':
        return "Feminino"

    return sexo


def valida_estadocivil(estadocivil):
    estadoCivil = estadocivil.lower()
    if estadoCivil not in ['S', 's', 'C', 'c', 'V', 'v', 'D', 'd']:
        raise ValueError('Valor Inválido.')

    if estadoCivil == 'S' or estadoCivil == 's':
        return "Solteiro"
    elif estadoCivil == 'C' or estadoCivil == 'c':
        return "Casado"
    elif estadoCivil == 'V' or estadoCivil == 'v':
        return "Viúvo"
    elif estadoCivil == 'D' or estadoCivil == 'd':
        return "Divorciado"

    return estadoCivil


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"

while True:
    try:

        nome_str = input('Qual o seu nome? ')
        nome = valida_nome(nome_str)

        idade_str = input('Qual a sua idade? ')
        idade = valida_idade(idade_str)

        salario_str = input('Qual o seu salario? ')
        salario = valida_salario(salario_str)

        sexo = input('Qual o seu sexo? ')
        sexo = valida_sexo(sexo)

        estadocivil = input('Qual o seu estado civil? ')
        estadoCivil = valida_estadocivil(estadocivil)

        print(f'\nNome: {nome_str}'
              f'\nIdade: {idade} ano{"s" if idade > 1 else ""}'
              f'\nSalario R$: {salario}'
              f'\nSexo: {sexo}'
              f'\nEstado Civil: {estadoCivil}')

        break
    except ValueError as ve:
        print(f'{RED}Erro: {ve}{RESET}')
    except KeyboardInterrupt:
        print(f'\n{RED}Operação interrompida pelo usuário.{RESET}')
        break
