C = int(input())
T = input().strip()

M = []
soma = 0.0

for linhas in range(12):
    linha = []
    for coluna in range(12):
        valor = float(input())
        linha.append(valor)
    M.append(linha)

for i in range(12):
    soma += M[i][C]

if T == 'S':
    print(f'{soma:.1f}')
if T == 'M':
    media = soma / 12
    print(f'{media:.1f}')