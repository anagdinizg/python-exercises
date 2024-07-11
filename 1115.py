conjunto = []

while True:
    par = input().strip()

    X, Y = map(int, par.split())

    if X == 0 or Y == 0:
        break

    conjunto.append((X, Y))

for X, Y in conjunto:
    if X >= 1 and Y >= 1:
        print('primeiro')
    elif X < 0 and Y >= 1:
        print('segundo')
    elif X < 0 and Y < 0:
        print('terceiro')
    elif X > 0 and Y < 0:
        print('quarto')