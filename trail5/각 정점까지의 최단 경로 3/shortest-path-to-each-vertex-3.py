import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def dijkstra(n, graph, start=1):
    INF = float('inf')

    min_heap = []
    dist = [INF] * (n + 1)

    dist[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        current_dist, curr = heapq.heappop(min_heap)

        if dist[curr] < current_dist:
            continue

        for w, next_node in graph[curr]:
            new_dist = current_dist + w
            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(min_heap, (new_dist, next_node))


    return dist[2:]

graph = {i: [] for i in range(1, n + 1)}
for u, v, w in edges:
    graph[u].append((w, v))

dist = dijkstra(n, graph)
for d in dist:
    print(d if d != float('inf') else -1)
