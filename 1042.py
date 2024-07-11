entrada = input()

x, y, z = map(int, entrada.split())

valores = [x, y, z]

ordenado = sorted(valores)

for valor in ordenado:
    print(valor)

print()

for valor in valores:
    print(valor)