X = int(input().strip())
Z = int(input().strip())

while Z <= X:
    Z = int(input().strip())

soma = X
contador = 1

while soma <= Z:
    contador += 1
    soma += X + contador - 1

print(contador)