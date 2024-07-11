valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    notaFormatada = str(nota).replace('.', ',')
    print(quantidade, "nota(s) de R$ {:.2f}".format(float(notaFormatada)).replace('.', ','))