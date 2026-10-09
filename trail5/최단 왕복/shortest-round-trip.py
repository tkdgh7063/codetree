import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a, b, w in edges:
    graph[a][b] = w

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if graph[i][k] == INF:
            continue

        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for start in range(1, n + 1):
    for end in range(1, n + 1):
        new_dist = graph[start][end] + graph[end][start]
        answer = min(answer, new_dist)

print(str(answer))
