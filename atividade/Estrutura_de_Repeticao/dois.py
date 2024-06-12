# Exercício 2
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

import re


def valida_senha(senha):
    # Define a expressão regular para a validação da senha
    regex = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=.{8,})"

    # Verifica se a senha corresponde à expressão regular
    if re.match(regex, senha):
        return True
    else:
        raise ValueError('A senha não atende aos critérios de segurança. Verifique os requisitos:'
                         '\n- 8 caracteres de comprimento'
                         '\n- Pelo menos uma letra maiúscula'
                         '\n- Pelo menos um dígito'
                         '\n- Pelo menos um caractere especial (@#$%^&+=)')


# Cores ANSI
RED = "\033[91m"
RESET = "\033[0m"

while True:
    try:

        senha = input('Informe uma senha: ')
        resultado = valida_senha(senha)
        if resultado is True:
            print('A senha atende aos critérios de segurança.')
        else:
            print(resultado)
        break
    except ValueError as ve:
        print(f'{RED}Erro: {ve}{RESET}')
    except KeyboardInterrupt:
        print(f'\n{RED}Operação cancelada pelo usuário.{RESET}')
        break
