L = int(input())
T = input().strip()

M = []

for linhas in range(12): # criando as linhas
    linha = []
    for coluna in range(12): # cada elemento da linha, preenchendo todas as 12 colunas
        valor = float(input())
        linha.append(valor)
    M.append(linha)

if T == 'S':
    print(f'{sum(M[L]):.1f}')
if T == 'M':
    media = sum(M[L]) / 12
    print(f'{media:.1f}')
