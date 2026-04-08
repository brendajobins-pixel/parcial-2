# ===== DESAFIO 06 - CONVERSÃO DE TEMPO =====

# Exibe um título
print('===== DESAFIO 06 - CONVERSÃO DE TEMPO =====')

# -------- PARTE 1: SEGUNDOS → HORAS, MINUTOS E SEGUNDOS --------

# Solicita a quantidade total de segundos
segundos = int(input('Digite a quantidade de segundos: '))

# Calcula quantas horas existem
horas = segundos // 3600

# Calcula o restante depois das horas
resto = segundos % 3600

# Calcula os minutos restantes
minutos = resto // 60

# Calcula os segundos restantes
segundos_restantes = resto % 60

# Exibe o resultado
print('Horas:', horas)
print('Minutos:', minutos)
print('Segundos:', segundos_restantes)

# -------- PARTE 2: HORAS, MINUTOS E SEGUNDOS → SEGUNDOS --------

# Solicita horas, minutos e segundos separadamente
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

# Converte tudo para segundos
# Fórmula: (horas * 3600) + (minutos * 60) + segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Exibe o resultado final
print('Total em segundos:', total_segundos)

