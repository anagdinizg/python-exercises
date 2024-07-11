quantidade = int(input())

num = 1

for i in range(quantidade):
    multiplicacao = num * num

    print(f"{num} {multiplicacao} {multiplicacao * num}")

    num += 1
