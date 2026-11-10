import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    mandarin = [list(map(int, input().split())) for _ in range(N)]  # 1은 귤, 2는 상한 귤

    queue = deque()

    visited = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mandarin[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 0

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and mandarin[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

    answer = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mandarin[i][j] == 1:
                if visited[i][j] == -1:
                    answer[i][j] = -2
                else:
                    answer[i][j] = visited[i][j]
            elif mandarin[i][j] == 0:
                answer[i][j] = -1
            else:
                answer[i][j] = 0

    for row in answer:
        print(*row)


if __name__ == "__main__":
    solve()
