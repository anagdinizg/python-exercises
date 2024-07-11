T = int(input())

for i in range(T):
    entrada = input()

    R1, R2 = map(int, entrada.split())

    menor_raio = R1 + R2

    print(menor_raio)
