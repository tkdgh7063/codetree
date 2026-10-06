import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
def dijkstra(n, graph, start, end):
    INF = float('inf')

    dist = [INF] * (n + 1)
    min_heap = []

    dist[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        current_dist, curr = heapq.heappop(min_heap)

        if dist[curr] > current_dist:
            continue

        for weight, next_node in graph[curr]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(min_heap, (new_dist, next_node))

    return dist[end]

graph = {i: [] for i in range(1, n + 1)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

answer = dijkstra(n, graph, A, B)
print(answer)
