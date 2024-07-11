valor1 = int(input())
valor2 = int(input())
soma = 0
maior = 0
menor = 0

if(valor1 > valor2):
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma += i

print(soma)
