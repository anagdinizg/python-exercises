N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0:
        quadrado = i * i
        print(f"{i}^2 = {quadrado}")