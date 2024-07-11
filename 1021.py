valor = float(input())

notas = int(valor)
moedas = int((valor - notas) * 100)

print("NOTAS:")
print(notas // 100, "nota(s) de R$ 100.00")
notas = notas % 100

print(notas // 50, "nota(s) de R$ 50.00")
notas = notas % 50

print(notas // 20, "nota(s) de R$ 20.00")
notas = notas % 20

print(notas // 10, "nota(s) de R$ 10.00")
notas = notas % 10

print(notas // 5, "nota(s) de R$ 5.00")
notas = notas % 5

print(notas // 2, "nota(s) de R$ 2.00")
notas = notas % 2

print("MOEDAS:")
print(notas, "moeda(s) de R$ 1.00")

print(moedas // 50, "moeda(s) de R$ 0.50")
moedas = moedas % 50

print(moedas // 25, "moeda(s) de R$ 0.25")
moedas = moedas % 25

print(moedas // 10, "moeda(s) de R$ 0.10")
moedas = moedas % 10

print(moedas // 5, "moeda(s) de R$ 0.05")
moedas = moedas % 5

print(moedas, "moeda(s) de R$ 0.01")
