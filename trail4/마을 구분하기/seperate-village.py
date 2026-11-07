n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 0 or visited[x][y] == 1:
        return False

    return True

def dfs(x, y):
    global num
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            num += 1
            dfs(nx, ny)


people = []

for i in range(n):
    for j in range(n):
        num = 1
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            people.append(num)

print(len(people))

people.sort()
for p in people:
    print(p)
