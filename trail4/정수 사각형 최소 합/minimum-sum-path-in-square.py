import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[None] * N for _ in range(N)]
    dp[0][-1] = grid[0][-1]
    for i in range(1, N):
        dp[0][N - i - 1] = dp[0][N - i] + grid[0][N - i - 1]
        dp[i][-1] = dp[i - 1][-1] + grid[i][-1]

    for i in range(1, N):
        for j in range(N - 2, -1, -1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j]

    print(str(dp[-1][0]) + "\n")

    return

if __name__ == "__main__":
    solve()
