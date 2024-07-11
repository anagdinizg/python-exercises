conjunto = []

par = int(input())

for i in range(par):
    X, Y = map(int, input().split())

    conjunto.append((X, Y))

for X, Y in conjunto:

    if Y == 0:
        print('divisao impossivel')
    else:
        divisao = X / Y
        print(f"{divisao:.1f}")
