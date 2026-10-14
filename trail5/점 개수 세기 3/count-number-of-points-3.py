import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
dots = set(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(Q)]

sorted_dots = sorted(list(dots))
mapper = {num: idx for idx, num in enumerate(sorted_dots)}

for a, b in edges:
    print(mapper[b] - mapper[a] + 1)
