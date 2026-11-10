import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 격자에서 사람마다 비를 피할 수 있는 가장 가까운 공간까지의 거리
    # 0은 이동 가능, 1은 이동 불가, 2는 사람, 3은 비를 피할 수 있는 공간

    N, H, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    shelters = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 3:
                shelters.append((i, j))

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, 1, -1]

    visited = [[-1] * N for _ in range(N)]
    answer = [[0] * N for _ in range(N)]

    def bfs():
        queue = deque()

        for px, py in shelters:
            queue.append((px, py))
            visited[px][py] = 0

        while queue:
            cx, cy = queue.popleft()

            for dx, dy in zip(dxs, dys):
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                    if grid[nx][ny] == 0 or grid[nx][ny] == 2:
                        # 이동 가능
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[cx][cy] + 1

    bfs()

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                answer[i][j] = visited[i][j]

    for row in answer:
        print(*row)


if __name__ == "__main__":
    solve()
