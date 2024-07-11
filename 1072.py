N = int(input())

count_in = 0
count_out = 0

for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        count_in += 1
    else:
        count_out += 1

print(f"{count_in} in")
print(f"{count_out} out")