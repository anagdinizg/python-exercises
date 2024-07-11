N = int(input())

for _ in range(N):
    v1, v2, v3 = map(float, input().split())
    media_ponderada = (v1 * 2 + v2 * 3 + v3 * 5) / (2 + 3 + 5)

    print(f'{media_ponderada:.1f}')
