n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if x > y:
        menor = y
        maior = x
    else:
        menor = x
        maior = y

    soma_impares = 0

    for num in range(menor + 1, maior):
        if num % 2 != 0:
            soma_impares += num

    print(soma_impares)