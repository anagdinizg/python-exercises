import math

primeiro = input()
segundo = input()

x1, y1 = map(float, primeiro.split())
x2, y2 = map(float, segundo.split())

distancia = math.sqrt(((x2 - x1) ** 2 ) + ((y2 - y1) ** 2))

print("{:.4f}".format(distancia))