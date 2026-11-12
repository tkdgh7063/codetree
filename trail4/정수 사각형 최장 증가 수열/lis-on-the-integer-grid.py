import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def solve():
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] = i, j에서 시작하는 수열의 최장 길이
    dp = [[-1] * N for _ in range(N)]

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if square[x][y] < square[nx][ny]:
                    # 다음 칸이 더 큰 경우
                    dp[x][y] = max(dfs(nx, ny) + 1, dp[x][y])

        return dp[x][y]

    answer = 1
    for i in range(N):
        for j in range(N):
            answer = max(answer, dfs(i, j))

    sys.stdout.write(str(answer) + "\n")

if __name__ == "__main__":
    solve()
