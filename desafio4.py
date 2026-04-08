# ===== DESAFIO 04 - CALCULADORA =====

# Exibe um título na tela
print('===== DESAFIO 04 - CALCULADORA =====')

# Solicita que o usuário digite o primeiro número
n1 = float(input('Selecione um número: '))

# Solicita que o usuário digite o segundo número
n2 = float(input('Selecione outro número: '))

# Solicita a operação desejada
operacao = input('Escolha uma operação [soma, subtração, multiplicação, divisão]: ')

# Verifica qual operação foi escolhida
if operacao == "soma":
    print('Resultado:', n1 + n2)

elif operacao == "subtração":
    print('Resultado:', n1 - n2)

elif operacao == "multiplicação":
    print('Resultado:', n1 * n2)

elif operacao == "divisão":
    # Verifica se o segundo número é zero (evita erro)
    if n2 != 0:
        print('Resultado:', n1 / n2)
    else:
        print('Erro: divisão por zero não é permitida')

else:
    # Caso a operação não exista
    print('Essa operação não existe')



