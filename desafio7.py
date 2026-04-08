# ===== DESAFIO 07 - CÁLCULO DE JUROS SIMPLES =====

# Exibe um título
print('===== DESAFIO 07 - CÁLCULO DE JUROS SIMPLES =====')

# Solicita o capital inicial
capital = float(input('Digite seu capital (C): '))

# Solicita a taxa de juros (em porcentagem)
taxa = float(input('Digite a taxa de juros (I): '))

# Solicita o tempo
tempo = float(input('Digite o tempo (T): '))

# Calcula os juros simples
# Fórmula: J = (C * I * T) / 100
juros = (capital * taxa * tempo) / 100

# Exibe o resultado
print('O valor dos juros é:', juros)
