J = 1

for I in [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]:
    for _ in range(3):
        print(f"I={I} J={J}")
        J += 1
    for _ in range(3):
        print(f"I={I} J={J}.2")
