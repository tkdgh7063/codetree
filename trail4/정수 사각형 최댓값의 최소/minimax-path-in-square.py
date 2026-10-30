import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[None] * N for _ in range(N)]
    dp[0][0] = grid[0][0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0], grid[i][0])
        dp[0][i] = max(dp[0][i - 1], grid[0][i])

    # 오른쪽, 아래 칸으로 이동
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

    print(str(dp[-1][-1]) + "\n")

    return

if __name__ == "__main__":
    solve()
