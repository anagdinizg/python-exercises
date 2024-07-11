N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())
    soma = 0
    contador = 0
    atual = X

    while contador < Y:
        if atual % 2 != 0:
            soma += atual
            contador += 1
        atual += 1

    print(soma)