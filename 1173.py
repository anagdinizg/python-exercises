valor = int(input())

N = []

for i in range(10):
    N.append(valor)
    valor *= 2

for i in range(10):
    print(f"N[{i}] = {N[i]}")