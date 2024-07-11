N = int(input())

sequencia = [0, 1]

while len(sequencia) < N:
    proximo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo)

print(' '.join(map(str, sequencia)))
