import sys

input = sys.stdin.readline

MAX_INT = 1_000_000

N, Q = map(int, input().split())
dot_set = set(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(Q)]  # A이상 B이하

dots = [1 if i in dot_set else 0 for i in range(MAX_INT + 1)]

prefix_sum = [0] * (MAX_INT + 1)
for i in range(1, MAX_INT + 1):
    prefix_sum[i] = prefix_sum[i - 1] + dots[i]

for a, b in lines:
    if a == 0:
        print(prefix_sum[b])
    else:
        print(prefix_sum[b] - prefix_sum[a - 1])
