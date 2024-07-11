entrada = input()

A, B, C = map(float, entrada.split())

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area_trapezio = ((A + B) * C) / 2
    print("Area = {:.1f}".format(area_trapezio))