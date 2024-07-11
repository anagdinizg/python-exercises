maior_valor = -1
posicao_maior = 1

for i in range(1, 101):
    numero = int(input())

    if numero > maior_valor:
        maior_valor = numero
        posicao_maior = i

print(maior_valor)
print(posicao_maior)