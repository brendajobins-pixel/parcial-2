#7 formula dos juros

capital = float(input("Digite seu capital (C): "))
taxa = float(input("Digite a tava de juros (I): "))
tempo = float(input("Digite o tempo (T): "))
juros = (capital*taxa*tempo) / 100
print("0 valor dos juros é", juros)
