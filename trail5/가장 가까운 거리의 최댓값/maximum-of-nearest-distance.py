import heapq

n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = float('inf')

def dijkstra(n, graph):
    dist = [INF] * (n + 1)
    min_heap = []

    dist[a] = 0
    dist[b] = 0
    dist[c] = 0
    heapq.heappush(min_heap, (0, a))
    heapq.heappush(min_heap, (0, b))
    heapq.heappush(min_heap, (0, c))

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

graph = {i: [] for i in range(1, n + 1)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

dist = dijkstra(n, graph)

max_dist = -1
for node in range(1, n + 1):
    if node in (a, b, c):
        continue
    if dist[node] != INF:
        max_dist = max(max_dist, dist[node])

print(max_dist)
