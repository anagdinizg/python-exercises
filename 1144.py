x, y = map(int, input().split())

primeiro = 1

while primeiro <= y:
    linha = []

    for _ in range(x):
        if primeiro <= y:
            linha.append(primeiro)
            primeiro += 1

    print(' '.join(map(str, linha)))
