pares = []
impares = []

for _ in range(15):
    valor = int(input())

    if valor % 2 == 0:
        pares.append(valor)

        if len(pares) == 5:
            for i in range(5):
                print(f"par[{i}] = {pares[i]}")
            pares = []

    else:
        impares.append(valor)

        if len(impares) == 5:
            for i in range(5):
                print(f"impar[{i}] = {impares[i]}")
            impares = []

if len(impares) > 0:
    for i in range(len(impares)):
        print(f"impar[{i}] = {impares[i]}")

if len(pares) > 0:
    for i in range(len(pares)):
        print(f"par[{i}] = {pares[i]}")
