positivos = 0
lista = []

for i in range(6):
    valor = float(input())

    if valor > 0:
        positivos += 1
        lista.append(valor)

media = sum(lista) / len(lista)
print(f"{positivos} valores positivos")
print(f"{media:.1f}")

