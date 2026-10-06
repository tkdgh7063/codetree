import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def dijkstra(n, graph, start=1):
    dist = [float('inf')] * (n + 1)
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

dist = dijkstra(n, graph, k)
for d in dist:
    print(d if d != float('inf') else -1)
