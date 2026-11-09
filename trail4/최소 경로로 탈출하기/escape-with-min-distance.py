from collections import deque
import sys

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    queue = deque()
    visited = [[-1] * M for _ in range(N)]

    def bfs(x, y):
        move = 0

        queue.append((x, y, move))
        visited[x][y] = move

        while queue:
            cx, cy, move = queue.popleft()

            move += 1

            for dx, dy in zip(dxs, dys):
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 1 and visited[nx][ny] == -1:
                        queue.append((nx, ny, move))
                        visited[nx][ny] = move

    bfs(0, 0)

    answer = visited[N - 1][M - 1]
    sys.stdout.write(str(answer) + "\n")

    return

if __name__ == "__main__":
    solve()
