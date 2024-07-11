entrada = input()

A, B, C = map(float, entrada.split())

triangulo = (A * C) / 2
circulo = 3.14159 * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))
