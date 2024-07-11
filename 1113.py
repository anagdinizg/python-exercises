conjunto = []

while True:
    par = input().strip()

    X, Y = map(int, par.split())

    if X == Y:
        break

    conjunto.append((X, Y))

for X, Y in conjunto:
    if X > Y:
        print('Decrescente')
    else:
        print('Crescente')
