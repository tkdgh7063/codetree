import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
v1, v2, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

INF = float('inf')
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for x, y, w in edges:
    graph[x][y] = min(graph[x][y], w)
    graph[y][x] = min(graph[y][x], w)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        if graph[i][k] == INF:
            continue

        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(1, N + 1):
    dist = graph[v1][i] + graph[v2][i] + graph[i][e]
    answer = min(answer, dist)

print(str(answer) if answer != INF else str(-1))
