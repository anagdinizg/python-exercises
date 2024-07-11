entrada = list(map(int, input().split()))

A = entrada[0]
N = None

for num in entrada[1:]:
    if num > 0:
        N = num
        break

while N is None or N <= 0:
    N = int(input().strip())

soma = 0

for i in range(N):
    soma += A + i

print(soma)