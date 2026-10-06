import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
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

graph = {i: [] for i in range(1, n + 1)}
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

dist = dijkstra(n, graph, B)
print(dist[A])


graph = [[0] * (n + 1) for _ in range(n + 1)]
for u, v, w in edges:
    graph[u][v] = w
    graph[v][u] = w

x = A
print(x, end=" ")

while x != B:
    for i in range(1, n + 1):
        if graph[x][i] == 0:
            continue

        if dist[i] + graph[i][x] == dist[x]:
            x = i
            break

    print(x, end=" ")
