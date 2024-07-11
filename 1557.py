while True:
    N = int(input().strip())

    if N == 0:
        break

    M = []

    for linha in range(N):
        linha_atual = []
        for coluna in range(N):
            if linha == 0:
                linha_atual.append(2 ** coluna)
            elif linha == coluna:
                linha_atual.append(2 ** (linha * 2))
            elif linha > coluna:
                linha_atual.append(2 ** (linha + coluna))
            else:
                linha_atual.append(2 ** (linha + coluna))
        M.append(linha_atual)

    valor = max(max(coluna) for coluna in M)
    T = len(str(valor))
    for linha in M:
        string = [f"{num:>{T}}" for num in linha]
        print(' '.join(string))
    print()
