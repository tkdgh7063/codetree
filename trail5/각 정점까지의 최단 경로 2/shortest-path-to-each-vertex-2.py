import sys
INF = sys.maxsize

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dist[i][i] = 0

for u, v, w in edges:
    dist[u][v] = min(dist[u][v], w)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for row in dist[1:]:
    for d in row[1:]:
        print(d if d != INF else -1, end=" ")
    print()
