while True:
    try:
        N = int(input())

        M = []
        for linha in range(N):
            linha_atual = []
            for coluna in range(N):
                if linha + coluna == N - 1:
                    linha_atual.append(2)
                elif linha == coluna:
                    linha_atual.append(1)
                else:
                    linha_atual.append(3)
            M.append(linha_atual)

        for linha in range(N):
            for coluna in range(N):
                print(f"{M[linha][coluna]}", end='')
            print()

    except EOFError:
        break
