S = 0.0
cima = 1
baixo = 1

while cima <= 39:
    valor = cima / baixo
    S += valor
    cima += 2
    baixo *= 2

print(f"{S:.2f}")