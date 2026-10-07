import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

INF = sys.maxsize

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

    return dist[1:]

graph = {i: [] for i in range(1, n + 1)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

dist = dijkstra(n, graph, n)
print(max(dist))
