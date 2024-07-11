primeiro = input()
segundo = input()

codigoA, numeroA, valorA = map(float, primeiro.split())
codigoB, numeroB, valorB = map(float, segundo.split())

total = (valorA * int(numeroA)) + (valorB * int(numeroB))

print("VALOR A PAGAR: R$ {:.2f}".format(total))