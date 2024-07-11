while True:
    N = int(input().strip())

    if N == 0:
        break

    M = []

    for linha in range(N):
        linha_atual = []
        for coluna in range(N):
            if linha == coluna:
                linha_atual.append(1)
            elif linha < coluna:
                linha_atual.append(coluna - linha + 1)
            elif linha > coluna:
                linha_atual.append(linha - coluna + 1)
        M.append(linha_atual)

    for linha in range(N):
        for coluna in range(N):
            print(f"{M[linha][coluna]:>3}", end='')
            if coluna < N - 1:
                print(' ', end='')
        print()
    print()
