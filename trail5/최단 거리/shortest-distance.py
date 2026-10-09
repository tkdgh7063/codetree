import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(M)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for start, end in queries:
    print(str(graph[start - 1][end - 1]) + "\n")
