n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [1, 0], [0, 1]
visited = [[0] * m for _ in range(n)]
answer = 0

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True

def can_go(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 0 or visited[x][y] == 1:
        return False

    return True

def dfs(x, y):
    global answer
    if x == n - 1 and y == m - 1:
        answer = 1
        return

    if answer:
        return

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

dfs(0, 0)
print(answer)
