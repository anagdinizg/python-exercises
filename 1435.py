while True:
    N = int(input().strip())

    if N == 0:
        break

    M = []

    for _ in range(N):
        linha_atual = []
        for _ in range(N):
            linha_atual.append(1)
        M.append(linha_atual)


    for linha in range(N):
        for coluna in range(N):
            acima = linha
            esquerda = coluna
            abaixo = N - linha - 1
            direita = N - coluna - 1
            distancia = min(acima, esquerda, abaixo, direita)
            M[linha][coluna] = distancia + 1

    for linha in range(N):
        for coluna in range(N):
            print(f"{M[linha][coluna]:>3}", end='')
            if coluna < N - 1:
                print(' ', end='')
        print()
    print()