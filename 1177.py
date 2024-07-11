T = int(input())

N = []

contador = 0

while len(N) <= 1001:
    for i in range(0, T):
        N.append(i)

for i in range(1001):
    print(f"N[{i}] = {N[i]}")