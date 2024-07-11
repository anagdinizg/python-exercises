T = int(input())

for _ in range(T):
    N = int(input())

    primeiro_termo, segundo_termo = 0, 1

    for _ in range(N):
        primeiro_termo, segundo_termo = segundo_termo, primeiro_termo + segundo_termo

    print(f"Fib({N}) = {primeiro_termo}")