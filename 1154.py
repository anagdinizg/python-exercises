idades = []
soma = 0
contador = 0

while True:
    N = int(input())

    if N < 0:
        break

    idades.append(N)
    soma += N
    contador += 1

media = soma / contador
print(f"{media:.2f}")




