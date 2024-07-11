J = 7

for I in range(1, 10, 2):
    print(f"I={I} J={J}")
    print(f"I={I} J={J - 1}")
    print(f"I={I} J={J - 2}")

    J += 2