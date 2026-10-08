import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 각 정점에서 X번 정점까지 왕복하여 최단 시간을 구함
# 그래프를 뒤집어 X번 정점에서 출발하여 각 정점까지의 최단 시간 측정
# 최단 시간 중 최대 시간 구하기
def dijkstra(n, graph, start):
    INF = float('inf')

    dist = [INF] * (n + 1)
    min_heap = []

    dist[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        current_dist, curr = heapq.heappop(min_heap)

        if dist[curr] < current_dist:
            continue

        for weight, next_node in graph[curr]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(min_heap, (new_dist, next_node))

    return dist

graph = {i: [] for i in range(1, N + 1)}
graph_reverse = {i: [] for i in range(1, N + 1)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph_reverse[v].append((w, u))

dist_from_X = dijkstra(N, graph, X)
dist_to_X = dijkstra(N, graph_reverse, X)
max_dist = -1
for start in range(1, N + 1):
    total_dist = dist_to_X[start] + dist_from_X[start]
    max_dist = max(max_dist, total_dist)

sys.stdout.write(str(max_dist))
