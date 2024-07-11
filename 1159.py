while True:
    X = int(input())

    if X == 0:
        break

    soma = 0
    contador = 0
    atual = X

    while contador < 5:
        if atual % 2 == 0:
            soma += atual
            contador += 1
        atual += 1

    print(soma)