import sys
from pprint import pprint

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
nums = [tuple(map(int, input().split())) for _ in range(M)]

conn = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    conn[i][i] = True

for a, b in nums:
    conn[a][b] = True

for k in range(1, N + 1):
    for i in range(1, N + 1):
        if not conn[i][k]:
            continue

        for j in range(1, N + 1):
            if conn[i][k] and conn[k][j]:
                conn[i][j] = True

for n in range(1, N + 1):
    cnt = sum(1 for i in range(1, N + 1) if not conn[n][i] and not conn[i][n])
    print(f"{cnt}\n")
