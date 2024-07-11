N = int(input())

for _ in range(N):
    X = int(input())

    if X <= 1:
        print(f"{X} nao eh primo")
    else:
        primo = True
        for i in range(2, X):
            if X % i == 0:
                primo = False
                break

        if primo:
            print(f"{X} eh primo")
        else:
            print(f"{X} nao eh primo")