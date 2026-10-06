import heapq

A, B, N = map(int, input().split())

bus_fare = []
stop_count = []
bus_stops = []

for _ in range(N):
    fare, count = map(int, input().split())
    bus_fare.append(fare)
    stop_count.append(count)
    bus_stops.append(list(map(int, input().split())))

# Please write your code here.
INF = float('inf')

max_node = max(A, B)
for bus_stop in bus_stops:
    max_node = max(max_node, max(bus_stop))

graph = [[(INF, INF)] * (max_node + 1) for _ in range(max_node + 1)]

for i in range(N):
    fare = bus_fare[i]
    stops = bus_stops[i]
    count = stop_count[i]

    for u_idx in range(count):
        for v_idx in range(u_idx + 1, count):
            u = stops[u_idx]
            v = stops[v_idx]
            time = v_idx - u_idx
            if (fare, time) < graph[u][v]:
                graph[u][v] = (fare, time)

def dijkstra(n, graph, start):
    dist = [(INF, INF)] * (n + 1)
    min_heap = []

    dist[start] = (0, 0)
    heapq.heappush(min_heap, (0, 0, start))

    while min_heap:
        cost, time, curr = heapq.heappop(min_heap)

        if (cost, time) > dist[curr]:
            continue


        for next_node in range(1, n + 1):
            edge_cost, edge_time = graph[curr][next_node]
            if edge_cost == INF:
                continue

            new_cost = cost + edge_cost
            new_time = time + edge_time

            if (new_cost, new_time) < dist[next_node]:
                dist[next_node] = (new_cost, new_time)
                heapq.heappush(min_heap, (new_cost, new_time, next_node))

    return dist

dist = dijkstra(max_node, graph, A)
ans_cost, ans_time = dist[B]

if ans_cost == float('inf'):
    print("-1 -1")
else:
    print(ans_cost, ans_time)
