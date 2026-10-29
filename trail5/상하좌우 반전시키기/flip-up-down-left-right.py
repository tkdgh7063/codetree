import sys

input = sys.stdin.readline
# print = sys.stdout.write

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 1행을 제외하고 버튼을 눌러 상하좌우 인접한 칸의 숫자를 반전
    # 1행을 반전시키려면 2행을 눌러야 함
    answer = 0
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for row_idx in range(1, N):
        for col_idx in range(N):
            if grid[row_idx - 1][col_idx] == 0:
                answer += 1
                for dx, dy in zip(dxs, dys):
                    nx = row_idx + dx
                    ny = col_idx + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        grid[nx][ny] = abs(grid[nx][ny] - 1)
                grid[row_idx][col_idx] = abs(grid[row_idx][col_idx] - 1)

    if sum(sum(row) for row in grid) != N * N:
        print("-1")
    else:
        print(answer)

    return


if __name__ == "__main__":
    solve()
