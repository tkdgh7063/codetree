import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
red1, red2 = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

INF = float('inf')

def dijkstra(n, graph, start):
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
for i, j, w in edges:
    graph[i].append((w, j))
    graph[j].append((w, i))

min_dist = INF
dist1 = dijkstra(N, graph, red1)
dist2 = dijkstra(N, graph, red2)

for start in range(1, N + 1):
    if start == red1 or start == red2:
        continue

    total_dist = dist1[start] + dist1[red2] + dist2[start]
    min_dist = min(min_dist, total_dist)

if min_dist == INF:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(min_dist))
