N = []

for i in range(20):
    valor = int(input())
    N.append(valor)

N.reverse()

for i in range(20):
    print(f"N[{i}] = {N[i]}")
