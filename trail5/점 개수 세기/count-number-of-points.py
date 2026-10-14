import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, Q = map(int, input().split())
dots = set(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

dots = sorted(list(dots))
mapper = {num: idx for idx, num in enumerate(dots)}

for start, end in queries:
    right_idx = bisect_right(dots, end)
    left_idx = bisect_left(dots, start)
    print(right_idx - left_idx)
