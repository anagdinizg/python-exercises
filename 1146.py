while True:
    valor = int(input())

    if valor == 0:
        break

    lista = []

    for i in range(1, valor + 1):
        lista.append(i)

    print(' '.join(map(str, lista)))
