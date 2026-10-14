import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
groups = [int(input()) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(Q)]

prefix_1 = [0] * (N + 1)
prefix_2 = [0] * (N + 1)
prefix_3 = [0] * (N + 1)

for i in range(1, N + 1):
    if groups[i - 1] == 1:
        prefix_1[i] = prefix_1[i - 1] + 1
        prefix_2[i] = prefix_2[i - 1]
        prefix_3[i] = prefix_3[i - 1]
    elif groups[i - 1] == 2:
        prefix_2[i] = prefix_2[i - 1] + 1
        prefix_1[i] = prefix_1[i - 1]
        prefix_3[i] = prefix_3[i - 1]
    else:
        prefix_3[i] = prefix_3[i - 1] + 1
        prefix_1[i] = prefix_1[i - 1]
        prefix_2[i] = prefix_2[i - 1]

for a, b in queries:
    a = max(0, a)
    b = min(b, N + 1)
    res1 = prefix_1[b] - prefix_1[a - 1]
    res2 = prefix_2[b] - prefix_2[a - 1]
    res3 = prefix_3[b] - prefix_3[a - 1]
    print(res1, res2, res3)
