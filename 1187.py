O = input().strip()

M = []
soma = 0.0
contador = 0

for _ in range(12):
    linha = []
    for coluna in range(12):
        valor = float(input())
        linha.append(valor)
    M.append(linha)

for i in range(12):
    for j in range(12):
        if i + j < 11 and i < j:
            soma += M[i][j]
            contador += 1

if O == 'S':
    print(f'{soma:.1f}')
elif O == 'M':
    media = soma / contador
    print(f'{media:.1f}')
