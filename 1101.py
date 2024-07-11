conjunto = []

while True:
    par = input().strip()

    M, N = map(int, par.split())

    if M <= 0 or N <= 0:
        break

    conjunto.append((M, N))

for M, N in conjunto:
    if M > N:
        maior = M
        menor = N
    else:
        maior = N
        menor = M

    soma = 0
    sequencia = []

    for i in range(menor, maior + 1):
        sequencia.append(i)
        soma += i

    string = ' '.join(map(str, sequencia))
    print(f"{string} Sum={soma}")