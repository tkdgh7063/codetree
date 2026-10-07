import heapq

n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Please write your code here.

# 출발칸을 정한 후 모든 점에 대한 최소 이동시간을 구함
# 그 중 최댓값을 구함
# 이 과정을 모든 점을 출발칸으로 정해 반복
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def dijkstra(n, grid, start):
    dist = [[float('inf')] * n for _ in range(n)]
    min_heap = []

    startX, startY = start
    dist[startX][startY] = 0
    heapq.heappush(min_heap, (0, (startX, startY)))

    while min_heap:
        current_time, (curr_x, curr_y) = heapq.heappop(min_heap)
        curr_char = grid[curr_x][curr_y]

        if dist[curr_x][curr_y] < current_time:
            continue

        for dx, dy in zip(dxs, dys):
            next_x = curr_x + dx
            next_y = curr_y + dy
            if 0 <= next_x < n and 0 <= next_y < n:
                new_char = grid[next_x][next_y]
                new_time = current_time + a if curr_char == new_char else current_time + b
                if new_time < dist[next_x][next_y]:
                    dist[next_x][next_y] = new_time
                    heapq.heappush(min_heap, (new_time, (next_x, next_y)))

    return dist

max_time = -1
for i in range(n):
    for j in range(n):
        dist = dijkstra(n, grid, (i, j))
        for row in dist:
            max_time = max(max_time, max(row))
print(max_time)
