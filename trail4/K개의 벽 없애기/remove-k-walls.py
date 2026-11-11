import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    r1, c1 = map(lambda x: int(x) - 1, input().split())
    r2, c2 = map(lambda x: int(x) - 1, input().split())

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    visited = [[[-1] * N for _ in range(N)] for _ in range(K + 1)]  # 부순 개수, 행, 열
    def bfs(x, y):
        queue = deque()
        move = 0
        remove = 0

        queue.append((x, y, remove))
        visited[remove][x][y] = move

        while queue:
            cx, cy, cr = queue.popleft()

            for dx, dy in zip(dxs, dys):
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[cr][nx][ny] == -1 and grid[nx][ny] == 0:
                        # 그냥 이동
                        queue.append((nx, ny, cr))
                        visited[cr][nx][ny] = visited[cr][cx][cy] + 1
                    elif cr < K and visited[cr + 1][nx][ny] == -1 and grid[nx][ny] == 1:
                        # 벽을 부수고 이동
                        queue.append((nx, ny, cr + 1))
                        visited[cr + 1][nx][ny] = visited[cr][cx][cy] + 1

    bfs(r1, c1)

    answer = min(
        (visited[k][r2][c2] for k in range(K + 1) if visited[k][r2][c2] != -1),
        default=-1
    )

    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
