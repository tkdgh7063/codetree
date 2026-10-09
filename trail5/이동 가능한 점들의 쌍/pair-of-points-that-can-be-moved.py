import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M, P, Q = map(int, input().split())
P -= 1
edges = [tuple(map(int, input().split())) for _ in range(M)]
pairs = [tuple(map(int, input().split())) for _ in range(Q)]

# 1 ~ P번 점은 빨간색
# A에서 B로 이동 시 경로에 빨간 점이 하나 이상 있어야 해당 경로 이동 가능
# 이동 경로의 최소 비용

INF = float('inf')
dist = [[INF] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for x, y, w in edges:
    x, y = x - 1, y - 1
    dist[x][y] = min(dist[x][y], w)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

total_dist = 0
total_cnt = 0
for x, y in pairs:
    distance = INF
    x, y = x - 1, y - 1
    for r in range(P + 1):
        distance = min(distance, dist[x][r] + dist[r][y])
    if distance != INF:
        total_cnt += 1
        total_dist += distance

print(str(total_cnt) + "\n" + str(total_dist))
