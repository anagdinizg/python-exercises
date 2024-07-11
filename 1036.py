import math

entrada = input()

A, B, C = map(float, entrada.split())

delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)

    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
