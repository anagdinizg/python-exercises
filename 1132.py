X = int(input())
Y = int(input())

if X > Y:
    menor = Y
    maior = X
else:
    menor = X
    maior = Y

lista = []

for num in range(menor + 1, maior):
    if num % 5 == 2 or num % 5 == 3:
        lista.append(num)

for num in lista:
    print(num)
