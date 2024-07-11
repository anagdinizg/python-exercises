entrada = input()

A, B = map(int, entrada.split())

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")