import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
groups = [int(input()) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(Q)]

prefix_sum = [[0] * (N + 1) for _ in range(3)]

for i in range(1, N + 1):
    for row in range(3):
        prefix_sum[row][i] = prefix_sum[row][i - 1]

    val = groups[i - 1]
    prefix_sum[val - 1][i] += 1

for a, b in queries:
    a = max(0, a) - 1
    b = min(b, N + 1)
    for row in range(3):
        res = prefix_sum[row][b] - prefix_sum[row][a]
        print(res, end=" ")
    print()
