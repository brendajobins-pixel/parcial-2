# ===== DESAFIO 02 - VERIFICANDO SE O NÚMERO É PAR =====

# Exibe um título na tela
print('===== DESAFIO 02 - VERIFICANDO SE O NÚMERO É PAR =====')

# Solicita que o usuário digite um número inteiro
numero = int(input('Escolha um número aleatório: '))

# Verifica se o número é par
# Um número é par quando o resto da divisão por 2 é igual a 0
if numero % 2 == 0:
    print('O número é par')
else:
    # Caso não seja par, automaticamente é ímpar
    print('O número é ímpar')
