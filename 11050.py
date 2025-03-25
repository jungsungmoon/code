N, K = map(int, input().split())

up = 1
down = 1
for k in range(K):
    up = N * up
    N = N - 1
    down = down * K
    K = K - 1

print(int(up/down))