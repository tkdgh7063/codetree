import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N = int(input())
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())

    visited = [[-1] * N for _ in range(N)]

    dxs = [1, 2, 2, 1, -1, -2, -2, -1]
    dys = [2, 1, -1, -2, -2, -1, 1, 2]
    def bfs(x, y):
        queue = deque()

        queue.append((x, y))
        visited[x][y] = 0
        while queue:
            cx, cy = queue.popleft()

            for dx, dy in zip(dxs, dys):
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[cx][cy] + 1

                        if nx == r2 and ny == c2:
                            return

                        queue.append((nx, ny))

    bfs(r1, c1)

    answer = visited[r2][c2]
    print(visited[r2][c2])

    return

if __name__ == "__main__":
    solve()
